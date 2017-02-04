sample_list = ['apple', 'banana', 'melon']
sample_dict = {
        'game': ['lol', 'startcraft'],
        'food': ['hamburger', 'pizza'],
        'color': ['red', 'green', 'blue']
        }

print('-- Exception1 --')
try:
    print(sample_list[2])
    print(sample_dict['fruits'])
except:
    print('리스트인덱스를 넘었거나 딕셔너리 키가 없음')


print('-- Exception2 --')
try:
    print(sample_list[2])
    print(sample_dict['fruits'])
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)

print('--Program terminate--')
