import parser
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

result = parser.get_webtoon_episode_list(WEBTOON_ID)
# result = parser.get_episode_list_from_page(WEBTOON_ID)

f = open('webtoon.html', 'w')
f.write('<html><body>')
for item in result:
    f.write('''<div>
    <a href="http://comic.naver.com{href}">{title}</a>
    | <span>{created}</span>
</div>'''.format(
        href=item['link'],
        title=item['title'],
        created=item['created']
    ))
f.write('</body></html>')
f.close()
