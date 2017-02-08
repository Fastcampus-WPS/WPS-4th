# HTML Day4

### Atom sass-autocompile 패키지 설치

**Ubuntu**  
`sudo apt-get install -y nodejs`   
`sudo apt-get install -y npm`

**macOS**  
`brew install node`

-

**nodejs 및 npm설치 이후**  

터미널에서 `node -v` 입력

> 정상출력:  
> `v7.?.?` 또는 `v4.?.?`

에러가 난다면  
`nodejs -v` 입력  

`node -v`로는 에러가 나지만 `nodejs -v`로는 버전이 정상적으로 출력되면  
 `sudo ln -s /usr/bin/nodejs /usr/bin/node`입력  
 
-

**`node -v`가 정상적으로 작동하는걸 확인했다면**

`node-sass` npm패키지 설치  
`sudo npm install node-sass -g`
