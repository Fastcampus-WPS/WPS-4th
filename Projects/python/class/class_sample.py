"""
projects/python에 가상환경을 적용한다
1. pyenv virtualenv <verision> <env_name>으로 환경생성
2. 해당 폴더에서 pyenv local <env_name>으로 가상환경 사용 설정
3. pyenv versions로 설정 적용되었는지 확인, pip list로 새 가상환경 상태인지 확인
4. pip install -r requirements.txt로 패키지 설치

5. 위와 별개로 projects/python/class폴더에만 사용되는 가상환경을 적용
"""
class Shop:
    _description = 'Python Shop Class'
    def __init__(self, name, shop_type, address):
        self._name = name
        self._shop_type = shop_type
        self._address = address

    def get_info(self):
        return '상점정보 ({})\n  유형: {}\n  주소: {}'.format(self._name, self._shop_type, self._address)

    def show_info(self):
        print(self.get_info())

    @classmethod
    def change_description(cls, new_description):
        cls._description = new_description

    
    @property
    def name(self):
        return self._name
        #return self.__name[:1] + '**'

    @name.setter
    def name(self, new_name):
        if '맥도날드' in new_name:
            print('그 이름은 사용할 수 없습니다')
            return
        self._name = new_name
        print('Set new name ({})'.format(self._name))


class Restaurant(Shop):
    def __init__(self, name, shop_type, address, avg_price):
        super().__init__(name, shop_type, address)
        self.avg_price = avg_price

    def get_info(self):
        ori = super().get_info()
        return ori.replace('상점', '음식점') + '\n  평균가격: {}'.format(self.avg_price)

s1 = Shop('홈플러스', '마트', '학동역')
r1 = Restaurant('프리모바치오바치', '이탈리안 레스토랑', '강남역', '2인기준 35000원')

s1.show_info()
r1.show_info()
