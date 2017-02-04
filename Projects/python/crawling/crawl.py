import parser
import requests
WEBTOON_ID = 651673
'''
네이버 웹툰 크롤러

환경 세팅
    1. alt + F12로 터미널 열기
    2. 터미널에서 pyenv version입력해서 가상환경이 적용된 터미널인지 확인
    3. pip 이용해서 BeautifulSoup4, requests설치
        pip install beautifulsoup4
        pip install requests
        pip install lxml
'''

# result = parser.get_webtoon_episode_list(WEBTOON_ID)
result = parser.get_episode_list_from_page(WEBTOON_ID)
# print(result)
# result = parser.get_webtoon_episode_list_by_range(WEBTOON_ID, 27, 42)


def save_file_from_url(path, url):
    # stream=True는 곧바로 파일을 다운로드 받지 않음을 의미
    r = requests.get(url, stream=True)
    # 요청이 성공적으로 완료되었을 경우(코드200)
    if r.status_code == 200:
        # 인자로 주어진 path의 파일을 열고 1024byte단위로 파일을 다운받아 기록함
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)

with open('webtoon.html', 'wt') as f:
    # thumbnail디렉토리가 존재하지 않을경우 만들어 줌
    import os
    if not os.path.exists('thumbnails'):
        os.makedirs('thumbnails')

    f.write('<html><body>')
    for item in result:
        # 파일을 저장할 path(문자열)
        # ex) thumbnail/thumb_163.jpg
        path = os.path.join('thumbnails', 'thumb_{}{}'.format(item['no'], item['file_ext']))

        # 저장할 path와 이미지 URL을 함수 인자로 넘김 (썸네일 이미지 파일 저장)
        save_file_from_url(path, item['url_img_thumbnail'])

        # 각각의 episode별로 HTML요소 작성
        f.write('''<div>
        <img src="{path}">
        <a href="http://comic.naver.com{href}">{title}</a>
        | <span>{created}</span>
    </div>'''.format(
            path=path,
            href=item.get('link', '#'),
            title=item['title'],
            created=item['created']
        ))
    f.write('</body></html>')
