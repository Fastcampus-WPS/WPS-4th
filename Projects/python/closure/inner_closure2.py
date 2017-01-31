level = 0

def outter(outter_param):
    def inner():
        outter_param[0] += 3
        print(outter_param)
    return inner

value = [50]
func1 = outter(value)
func1()
func1()
