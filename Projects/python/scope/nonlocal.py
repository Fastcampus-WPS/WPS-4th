'''
a 또는 i로 입력모드 전환
입력 완료 후 esc눌러 편집모드 나오기
:w로 저장 또는 :wq로 저장하고 나오기
'''
champion = 'Lux'

def local1():
    champion = 'Ahri'
    print('local1 locals() : {}'.format(locals()))

    def local2():
        nonlocal champion
        champion = 'Ezreal'
        champion2 = 'local2 Ezreal'
        print('local2 locals() : {}'.format(locals()))

        def local3():
            nonlocal champion
            nonlocal champion2
            champion = 'Zed'
            champion2 = 'local3 Zed'

        local3()
        print('after local3, local2 locals() : {}'.format(locals()))

    local2()
    print('after local2, 3, local1 locals() : {}'.format(locals()))

print('global locals() : {}'.format(locals()))
local1()
