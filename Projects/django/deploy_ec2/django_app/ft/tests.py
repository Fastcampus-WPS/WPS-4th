from django.test import LiveServerTestCase
from selenium import webdriver


class BaseTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def make_url(self, url):
        return '{}{}'.format(self.live_server_url, url)


class NewVisitorTest(BaseTestCase):
    def test_first_page_show_hello_world(self):
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Hello, world!', page_text)
