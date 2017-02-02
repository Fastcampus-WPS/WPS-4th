# 프로젝트 설정


## pyenv, virtualenv 관련

### 가상환경 생성

```
pyenv virtualenv <version> <env_name>
```


### 가상환경을 해당 폴더에서 사용하도록 지정

```
pyenv local <env_name>
```

### 현재 가상환경이 적용되어있는지 확인

```
pyenv version
```

## pip 관련

### requirements가 있을 경우 설치

```
pip install -r requirements.txt
```

### ImportError: No module named 'packaging'

```
pip install --upgrade pip
```
실행 후 다시 `install`

### Could not import setuptools which is required to install from a source distribution.

```
pip install -U setuptools
```
실행 후 다시 `install`

