# Q&A

## 문자열에 replace를 쓰면 수정이 되는데, 문자열이 불변하다는 것의 의미는?

문자열의 `replace`함수를 사용하면 해당 문자열에서 특정 값이 변환된 **새로운** 문자열 변수가 리턴됩니다.  

```python
>>> champion = 'Lux'
>>> champion.replace('L', 'A')
'Aux'
>>> print(champion)
Lux
```

## macOS에서 .pyenv폴더 지워도 되나요

네. `rm -rf .pyenv` 명령어를 사용하시면 됩니다.

`-r` : 디렉토리를 삭제  
`-f` : 삭제확인 하지 않음


## slice연산

```python
In [47]: sample_list2[-1:-4:-1]
Out[47]: ['Dec', 'Nov', 'Oct']

In [48]: sample_list2[-1]
Out[48]: 'Dec'

In [49]: sample_list2[-2]
Out[49]: 'Nov'

In [50]: sample_list2[-3]
Out[50]: 'Oct'

In [51]: sample_list2[-4]
Out[51]: 'Sep'
```

sample\_list2 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']일때, 
뒤에서부터 거꾸로 'Dec','Nov','Oct' 를 출력하고 싶을때 slice문은 sample_list2[-1:-3:-1]이 되어야 하지 않나요?
왜 sample\_list2[-1:-4:-1]를 실행해야 제가 생각한 결과가 나오는지 궁금합니다.

-

end문은 '미만'을 뜻하므로, -3번째까지 포함하고 싶다면 -4를 적어주어야 합니다.

