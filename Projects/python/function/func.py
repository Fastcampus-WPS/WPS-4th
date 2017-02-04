def shop(name):
    name = name

    def inner():
        nonlocal name
        print(name)
    return inner

s = shop('abc')
print(s.name)
