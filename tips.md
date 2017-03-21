## 셸 설정

#### 파이참 실행 alias

```shell
alias py="open -a /Applications/PyCharm\ CE.app/Contents/MacOS/pycharm"
```

사용시 `py .`입력시 현재폴더를 기준으로 파이참 실행


## sass-autocompile이 작동하지 않을 때

### node-sass 재설치

```
sudo npm uninstall node-sass -g
sudo npm install node-sass
atom 재시작
```

### node 재설치 (이후 node-sass재설치)

**macOS**  

```
brew uninstall node
brew install node
```

**Ubuntu**  

```
sudo apt-get --purge autoremove npm
sudo apt-get --purge autoremove nodejs
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
```