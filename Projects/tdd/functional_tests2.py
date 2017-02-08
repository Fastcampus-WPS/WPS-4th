from selenium import webdriver
import unittest


# 테스트 시 AssertionError 대신 좀 더 자세한 정보가 필요
# 브라우저를 자동으로 열고 닫고싶음
# unittest모듈이 이를 지원함
class InitTest(unittest.TestCase):
    # 각 테스트 메서드 전에 호출
    def setUp(self):
        self.browser = webdriver.Chrome()
        # 브라우저 구동시간을 기다려줌
        self.browser.implicitly_wait(3)

    # 각 테스트 메서드 후에 호출
    def tearDown(self):
        self.browser.quit()

    # 테스트할 메서드는 test_로 시작하도록 함
    def test_main_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)


if __name__ == '__main__':
    # unittest 테스트 실행함수를 실행
    unittest.main()
