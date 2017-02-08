from django.test import TestCase


# 테스트 실패시를 보여줌
class BadTest(TestCase):
    def test_bad_function(self):
        self.assertEqual(1 + 1, 5)
