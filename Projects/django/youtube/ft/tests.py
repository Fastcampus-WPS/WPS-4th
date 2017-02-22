"""
170221 숙제
1. video app을 생성하고
2. 유튜브 영상의 정보를 저장할 수 있는 Model구현, Migrations
3. POST요청을 받으면 요청에서 온 키워드로 유튜브를 검색 후 결과를 DB에 저장하는 View구현
    방금 작성한 code/youtube.py파일의 내용을 하나의 함수로 구현

    3-1. GET요청시에는 검색 input이 하나 있는 페이지를 단순 render
        3-1-1. 해당 페이지에는 form요소가 있어야 함
    3-2. POST요청은 GET요청에 있는 form을 통해서 이루어짐
        3-2-1. POST요청으로는 keyword 또는 q라는 이름으로 검색키워드 정보를 전달
        3-2-2. 전달받아온 키워드를 이용해 유튜브 검색 API실행
        3-2-3. 이후 해당 결과를 적절히 순회하며 DB에 저장
        3-2-4. 저장되어있는 모든 데이터를 템플릿에 전달
4. 위 View를 나타낼 수 있는 Template구현
5. View와 Template연결
6. 실행해보기^^

170222 AbstractUser를 상속받아 CustomUser구현
1. member app생성
2. AbstractUser를 상속받은 MyUser를 생성
3. AUTH_USER_MODEL에 등록
4. 마이그레이션 해본다

**extra
5. Django admin에 MyUser를 등록
6. 기본 UserAdmin을 상속받아 사용자 관련 모듈이 잘 작동하도록 설정
    (기본값으로 두면 패스워드 해싱등이 동작하지 않음)
"""
from django.test import LiveServerTestCase
from selenium import webdriver


class SearchTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_display_search_view(self):
        self.browser.get(self.live_server_url)
        self.assertEqual('YouTube', self.browser.title)