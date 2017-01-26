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


