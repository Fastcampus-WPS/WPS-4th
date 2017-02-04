class Shop:
    def __init__(self, name):
        self.__name = name

    @property
    def type(self):
        return self.__name

    @staticmethod
    def print_static():
        print('static!')


shop = Shop('ABC')
print(shop.type)
print(type(shop.type))


Shop.print_static()
shop.print_static()
