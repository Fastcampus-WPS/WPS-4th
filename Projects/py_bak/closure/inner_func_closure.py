level = 0
def outter():
    global level
    level = 50

    def inner():
        global level
        level += 3
        print(level)

    return inner

func = outter()
func()
