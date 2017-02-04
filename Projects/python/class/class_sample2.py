class User:
    def __init__(self, name):
        self.name = name

    def eat_something(self, item):
        item.eat()

class Something:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{}는 뭔지 모르니 먹을수가없다!'.format(self.name))


class Food(Something):
    def eat(self):
        print('{}를 먹었다. 배가부르다'.format(self.name))


class Drink(Something):
    def eat(self):
        print('{}를 마셨다. 갈증이 해소된다!'.format(self.name))


'다형성 : 동일한 실행에 대하여 다른 동작을 수행할 수 있도록 하는 것'
user = User('이한영')
s1 = Something('무언가')
food1 = Food('햄버거')
drink1 = Drink('포카리스웨트')

user.eat_something(s1)
user.eat_something(food1)
user.eat_something(drink1)
