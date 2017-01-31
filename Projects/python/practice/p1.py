def what_fruit(color):
    '''
    color값을 받아 어떤 과일에 해당하는지 문자열 형태로 리턴해준다
    '''
    if color == 'red':
        return 'apple'
    elif color == 'yellow':
        return 'banana'
    elif color == 'green':
        return 'melon'
    else:
        return 'I don\'t know'

help(what_fruit)
result = what_fruit('red')
result2 = what_fruit('green')
result3 = what_fruit('blue')

print(result, result2, result3)
