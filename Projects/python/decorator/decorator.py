def print_args(func):
    def inner_func(*args, **kwargs):
        print('args : {}'.format(args))
        return func(*args, **kwargs)
    return inner_func

def decorator_test(func):
    def inner_func(*args, **kwargs):
        print('test_inner')
        return func(*args, **kwargs)
    return inner_func

@print_args
@decorator_test
def multi(arg1, arg2):
    result = arg1 * arg2
    print(result)
    return result

@decorator_test
@print_args
def divide(arg1, arg2):
    result = arg1 / arg2
    print(result)
    return result

multi(3, 5)
divide(10, 2)


