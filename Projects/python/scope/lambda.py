import string
for char in string.ascii_lowercase:
    if char > 'i':
        print(char.upper())
    else:
        print(char)

for char in string.ascii_lowercase:
    print((lambda x : x.upper() if x > 'i' else x)(char))


