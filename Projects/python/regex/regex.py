import re
source = 'Lux, the Lady of Luminosity'
print('source : %s' % source)
print('--p1--')
p1 = re.compile('Lux')
m1 = re.match(p1, source)
if m1:
    print(m1.group())

print('--p2--')
p2 = re.compile('Lady')
m2 = re.match(p2, source)
if m2:
    print(m2.group())

print('--p3--')
p3 = re.compile('.*Lady')
m3 = re.match(p3, source)
if m3:
    print(m3.group())


print('--search--')
p4 = re.compile('Lady')
m4 = re.search(p4, source)
if m4:
    print(m4.group())

print('--findall--')
p5 = re.compile('y')
m5 = re.findall(p5, source)
if m5:
    print(m5)

print('--findall2--')
p6 = re.compile('y..')
m6 = re.findall(p6, source)
if m6:
    print(m6)


print('--split--')
s2 = '민아,혜리,소진,유라'
s2_list = s2.split(',')
print(s2_list)

m = re.split('.o.', source)
print(m)


print('--sub--')
s2 = source.replace('L', 'A')
print(s2)

m = re.sub('L', 'A', source)
print(m)


import string
printable = string.printable
printable += '가나다라마바사아자차카타파하'
print(printable)

m = re.findall('\w', printable)
print(m)
m = re.findall('\W', printable)
print(m)

pattern_list = [r'\d', r'\D', r'\w', r'\W', r'\s', r'\S', r'\b', r'\B']

for p in pattern_list:
    print('Pattern {}'.format(p))
    print(re.findall(p, printable))
    print('')


p = re.compile('Lux|Lady')
print(re.findall(p, source))
