import re

class NotMatchedException(Exception):
    def __init__(self, re_pattern=None, source=None):
        # 만약 인자로 주어진 re_pattern객체가 
        # re._pattern_type형 객체라면
        # (컴파일된 정규표현식 패턴 객체)
        # self.pattern_str속성에 re_pattern.pattern값을 할당
        if isinstance(re_pattern, re._pattern_type):
            self.pattern_str = re_pattern.pattern

        # re_pattern객체가 str(문자열)형일 경우
        # self.pattern_str속성에 해당 값을 그대로 할당
        elif isinstance(re_pattern, str):
            self.pattern_str = re_pattern

        self.source = source

    def __str__(self):
        return 'Pattern("{}") is not matched in Source("{}")'.format(self.pattern_str, self.source)


def search_from_source(pattern, source):
    m = re.search(pattern, source)
    if m:
        return m
    else:
        raise NotMatchedException(pattern, source)


try:
    print('--try search_from_source--')
    source = 'Lux, the Lady of Luminocity'
    pattern_str1 = 'Ladyyyy'
    pattern_str2 = r'\w+\s+Lady\s+\w+'
    pattern = re.compile(pattern_str1)
    m = search_from_source(pattern, source)
except NotMatchedException as e:
    print(e)
else:
    print('  result : {}'.format(m.group()))
finally:
    print('--end search_from_source--')


print('--Program terminated--')
