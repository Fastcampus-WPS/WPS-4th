from django.core.urlresolvers import resolve
from django.test import TestCase

from note.tests.tests3.blog.views import index


class SiteTest(TestCase):
    # 루트 URL이 index view와 연결되어있는지 테스트
    def test_root_url_resolves_to_index_view(self):
        # resolve메서드를 사용해 해당 URL패턴과 일치하는 view함수가 있는지 검사
        view = resolve('/')
        # 결과값의.func에 view함수가 들어옴
        self.assertEqual(view.func, index)

'''
TypeError: view must be a callable or a list/tuple in the case of include().
    view의 형태가 올바르지 않음
'''