def square_or_multi(arg1, arg2=None):
    if arg2 is None:
        print(arg1 * arg1)
    else:
        print(arg1 * arg2)

def square_or_multi2(*args):
    length = len(args)
    if length == 1:
        print(args[0] * args[0])
    elif length == 2:
        print(args[0] * args[1])
    else:
        print('args invalid')


square_or_multi(3)
square_or_multi(10, 5)

square_or_multi2(10)
square_or_multi2(10, 20)
square_or_multi2(10, 20, 30)
