class Shop:
    desc = 'Shop desc'
    def __init__(self, name, shop_type):
        self.name = name
        self.__shop_type = shop_type
        self.abc = 'abc'

    @classmethod
    def change_desc(cls, desc):
        cls.desc = desc

    @property
    def info(self):
        return '상점정보 %s' % self.name

    def show_info(self):
        print(self.info)

    @property
    def type(self):
        return self.abc


shop = Shop('name', 'shop_type')
shop.show_info()
ii = isinstance(shop, Shop)
print(ii)

print(shop.type)