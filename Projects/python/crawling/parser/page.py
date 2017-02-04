import math
from .communication import get_soup_from_url


def get_soup_from_naver_webtoon_by_page(webtoon_id, page=1):
    '''
    네이버웹툰의 만화 고유 ID(URL GET paramter중 titleId)와
    페이지넘버(URL GET paramter중 page)를 받아
    해당만화의 페이지(num)의 HTML을 BeautifulSoup객체로 반환
    :param webtoon_id: 네이버웹툰 고유 ID
    :param page: 주어지지 않을 경우 1페이지를 요청함
    :return: BeautifulSoup object
    '''
    # 네이버웹툰 사이트 주소
    url = 'http://comic.naver.com/webtoon/list.nhn'
    # GET parameters로 전달할 값들의 dict
    params = {'titleId': webtoon_id, 'page': page}
    return get_soup_from_url(url, params)


def get_webtoon_recent_episode_number(webtoon_id):
    '''
    웹툰의 첫 페이지, 첫 화 (가장 최신화)의 링크에서
    가장 최신화의 번호(=현재까지 연재한 횟수)를 가져온다
    :param webtoon_id: 웹툰 고유 ID
    :return: 최신 에피소드 번호(=총 연재횟수)
    '''
    soup = get_soup_from_naver_webtoon_by_page(webtoon_id)
    tr_list = soup.find_all('tr')
    recent_episode_number = None
    # 만화목록 페이지의 테이블에서 매 row를 순회하며
    for tr in tr_list:
        # class가 title인 td요소를 찾는다
        td = tr.find('td', class_='title')
        if td:
            # 링크주소가 있는 a요소
            a = td.find('a')
            # a요소의 href속성
            href = a.get('href')

            import re
            # 정규표현식, 아무문자열이나 반복되다가 ?no=또는 &no=이후의 숫자와 매칭된다
            p = re.compile(r'.*[?&]no=(\d+).*')
            m = re.match(p, href)
            # 링크주소에서 정규표현식의 패턴이 매치되었을 때
            if m:
                # 매치된 숫자를 recent_episode_number에 할당하고 반복문 종료
                recent_episode_number = m.group(1)
                break

    # HTML을 파싱한 결과는 문자열이므로 정수형으로 형변환 후 리턴
    return int(recent_episode_number)


def get_episode_list_from_page(webtoon_id, page=1):
    soup = get_soup_from_naver_webtoon_by_page(webtoon_id, page)
    # 리턴할 리스트
    episode_list = []

    # 첫 번째 tr요소는 기대하는 형태를 가지고 있지 않으므로 (td 4개를 포함하고 있지 않음) 제외
    tr_list = soup.find_all('tr')
    for index, tr in enumerate(tr_list):
        td_list = tr.find_all('td')
        # 각 row가 자식 td요소를 4개 미만으로 가지면 loop건너뜀
        if len(td_list) < 4:
            continue
        # 각 row가 몇 개의 td를 가지고 있는지 테스트
        # print('{} : {}'.format(index, len(td_list)))

        td_thumbnail = td_list[0]
        td_title = td_list[1]
        td_rating = td_list[2]
        td_created = td_list[3]

        url_img_thumbnail = td_thumbnail.a.img['src']
        # 파일경로에서 파일 이름과 확장자를 구분함
        import os
        _, ext = os.path.splitext(url_img_thumbnail)

        title = td_title.get_text(strip=True)
        created = td_created.get_text(strip=True)
        link = td_title.find('a').get('href')
        import re
        # 정규표현식, 아무문자열이나 반복되다가 ?no=또는 &no=이후의 숫자와 매칭된다
        p = re.compile(r'.*[?&]no=(\d+).*')
        m = re.match(p, link)
        no = m.group(1)

        cur_episode = {
            'url_img_thumbnail': url_img_thumbnail,
            'file_ext': ext,
            'title': title,
            'no': no,
            'link': link,
            'created': created,
        }
        episode_list.append(cur_episode)
    return episode_list


def get_webtoon_episode_list(webtoon_id):
    '''
    특정 웹툰의 모든 에피소드 리스트를 리턴
    :param webtoon_id: 웹툰 고유 ID
    :return: 에피소드 dict의 list
    '''
    page_count = 10
    total_episode_list = []

    total_episode_number = get_webtoon_recent_episode_number(webtoon_id)
    import math

    # 총 페이지 수
    total_page_number = math.ceil(total_episode_number / page_count)

    # 각 페이지를 순회하며 리스트를 합침
    for i in range(total_page_number):
        cur_page_num = i + 1
        # 페이지번호의 HTML soup객체를 인자로 전달해서 episode dict list를 가져온다
        cur_episode_list = get_episode_list_from_page(webtoon_id, cur_page_num)
        # 현재 페이지에서 가져온 episode list를 total_episode_list리스트에 넣어준다
        total_episode_list.extend(cur_episode_list)

    for episode in total_episode_list:
        print(episode)
    return total_episode_list


def get_webtoon_episode_list_by_range(webtoon_id, start, end):
    # 웹툰ID, start, end를
    # 받아서
    # 가장
    # 최근부터
    # start만큼의
    # offset부터
    # end의
    # offset까지
    # 해당하는
    # episode들의
    # 정보
    # 리스트를
    # 리턴해주는
    # 함수
    '''
    page_count = 10 (한 페이지당 10개의 요소가 있다)
    구할수 있는 정보 : 최신화의 no
    페이지당 10개씩 episode list
        -> 최신화의 no, start, end를 비교해서 어떤 page를 가져와야 하는지
    start가 0일때 최신화부터

    no = 183
    start = 27
    end = 42

    -> 156 ~ 141
    start_no = 156
    end_no = 141
        -> no 156 ~ 142화까지 (141화는 end로 미만처리)

    start / page_count = 2.5 => 1페이지에 10개, 2페이까지 20개, 3페이지 에 start에 있는 부분이 해당
    end / page_count = 4.2 => 5페이지에 end에 있는 부분이 해당

    start, end의 offset을 page_count로 나눈 소수를 올림처리하면 start와 end가 해당하는 페이지 번호가 나옴
    '''
    # 마지막에 리턴해줄 episode dict 리스트
    total_episode_list = []
    # 한 페이지에 episode 몇 개씩 들어있는지
    page_count = 10
    # start offset의 episode가 몇 번째 page에 해당하는지
    start_page = math.ceil(start / page_count)
    # end offset의 episode가 몇 번째 page에 해당하는지
    end_page = math.ceil(end / page_count)

    # start가 27일 경우, 7이 남음 -> 3번째 페이지에서 7번째 요소가 start offset에 해당하는 episode
    # 따라서 해당 페이지의 episode_list[start_slice_num:]로 자르면
    # start보다 앞에 있는 episode들은 잘려나감
    start_slice_num = start % page_count

    # end가 42일 경우 2가 남음 -> 4번째 페이지에서 2번째 요소가 end offset에 해당하는 episode
    # 따라서 해당 페이지의 episode_list[:end_slice_num]로 자르면
    # end를 포함한 episode들은 잘려나감 (조건에서 end는 미만으로 처리)
    end_slice_num = end % page_count

    # start_page부터 end_page까지 순회해야하므로 range의 마지막은 미만처리되니 끝 번호에 1추가
    for num in range(start_page, end_page + 1):
        # 해당 페이지의 episode_list를 받아와서
        cur_episode_list = get_episode_list_from_page(webtoon_id, num)

        # 만약에 첫 페이지일 경우
        if num == start_page:
            # 받아온 episode_list를 start_slice_num을 시작 오프셋으로 잘라줌
            cur_episode_list = cur_episode_list[start_slice_num:]
        # 만약에 마지막 페이지일 경우
        elif num == end_page:
            # 받아온 episode_list를 end_slice_num을 끝 오프셋으로 잘라줌
            cur_episode_list = cur_episode_list[:end_slice_num]
        # 리턴할 total_episode_list에 연장시킴
        total_episode_list.extend(cur_episode_list)

    for episode in total_episode_list:
        print(episode)

    # 최신화를 기준으로 start이상, end미만의 episode_list를 리턴하게 됨
    return total_episode_list