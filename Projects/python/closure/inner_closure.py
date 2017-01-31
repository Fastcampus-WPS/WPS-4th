level = 0
def outter():
    level = 50

    def inner():
        nonlocal level
        level += 3
        print(level)
    return inner

func1 = outter()
print('func1 id : %s' % id(func1))
func1()
func1()
func1()
print('')
func2 = outter()
print('func2 id : %s' % id(func2))
print('func1 id : %s' % id(func1))
func2()
func2()
