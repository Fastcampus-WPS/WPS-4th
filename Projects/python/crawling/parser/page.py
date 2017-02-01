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

        title = td_title.get_text(strip=True)
        created = td_created.get_text(strip=True)
        link = td_title.find('a').get('href')

        cur_episode = {
            'title': title,
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

    # for episode in total_episode_list:
    #     print(episode)
    return total_episode_list
