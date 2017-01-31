global_level = [100]

def arguments_level_add(value):
    '''
    인자로 전달받은 값을 value라는 parameter로 사용
    value parameter의 값을 30증가시키고 출력
    '''
    value[0] += 30
    print('arguments_level_add, value : %s' % value)

def global_level_add():
    '''
    global scope의 global_level변수의 값을 30 증가시키고 출력
    '''
    global global_level
    global_level[0] += 30
    print('global_level_add, value : %s' % global_level)

def show_global_level():
    '''
    global scope의 global_level변수 값을 출력
    '''
    print('global_level : %s' % global_level)

show_global_level()
arguments_level_add(global_level)
show_global_level()
global_level_add()
show_global_level()


