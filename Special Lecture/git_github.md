# TIL☘

2021년 12월 30일

## Git, Github란

개발자들의 헙엽을 위한 도구

* Git
  * Git을 이용한 버전 관리 프로그램
  * 분산 버전 관리 : 중앙 컴퓨터에 문제가 생겨도 각자의 버전이 컴퓨터에 저장이 되어있어 복구가 가능하다.

* Github
  * 포트폴리오 서비스 (온라인 공유 서비스 -> 연결시 인터넷 필요)



## 접점(Interface)

두 개의 다른 존재를 이어주는 매개체

* GUI(Graphic User Interface) : 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식
* CLI(Command Line Interface) : 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식



## Git Bash

창을 켜고 확인해야하는 것 => ⭐내가 어디에 있는지 확인하기 !!⭐

~ (필터) : 현재 위치를 알려준다. ~ : 홈폴더(사용자계정)

<리눅스 명령어>

* data		현재의 시간 확인한다
  ls			 리스트, 폴더 안의 내용을 리스트해 보여줌
  ls -a		 숨긴 폴더, 파일을 보여준다 (ls의 숨긴 폴더와 파일을 보여줌)
  . 			  현재 위치
  ..			  상위 위치
  cd			change directory 폴더를 이동한다 (cd만 치면 홈폴더로 감)
  clear	   내용을 위로 밀어준다
  start		폴더/파일을 연다

  touch a.txt     파일을 만든다 (a.txt 파일을 만듦)
  mkdir test	  폴더를 만든다 (test 폴더를 만듦)
  => 한줄에 여러개 입력 가능   예) touch a.txt b.txt c.txt

* 삭제명령어
  rm a.txt		파일을 삭제한다 (a.txt 파일을 삭제)
  rm -r test	 폴더를 삭제한다 (test 폴더를 삭제)
  rm *.txt		확장자를 지정해 파일을 삭제한다 (txt 파일을 삭제)
  rm -rf  *		현재 폴더의 모든 것을 삭제한다 (f : force, * : asterisk all을 의미)

* 절대경로 : 어디든 바뀌지 않음 (강남역은 서울 강남구 강남대로 396)
  상대경로 : 내가 있는 위치에서 목적지의 위치 (강남역은 걸어서 600m가고 우회전)





## 깃허브

* TIL (Today I Learned)
* MD (Mark Down) : 개발자들의 문서 작성 양식 & 문법
* README.md : 대문 소개 페이지



## Typora

문법을 기입하면 자동적으로 변환해주는 프로그램

* HTML (Hyper Text Markup Language) 
  : 순서가 정해지지 않은 글자들을 태그로 감싸서 논리적으로 컴퓨터에 전달하는 언어 
  <h1>예)큰제목</h1>

* `#`개수로 폰트의 크기를 키우는 개념이 아니고, 문서의 논리적 흐름의 뼈대를 작성

  * Typora에서 #와 `<h1>`의 차이

    Typora에서는 #은 제목을 나타내주며 트리에 반영이 된다.

    Typora는 HTML 문법을 보여주는 기능이 있어 HTML 태그인 `<h1>`로 작성해도 #을 쓴것처럼 똑같이 나오지만 개요에서 제목의 역할은 하지 않는다.

* `ctrl + /`를 입력하면 원형을 볼 수 있다
* `window + .`를 입력하면 이모티콘을 사용할 수 있다

## Vscode

* `ctrl + `(backtick)`	터미널 열기/닫기
* 터미널의 휴지통과 X의 차이
  * 휴지통 : Kill terminal, 터미널 삭제
  * X : 가독성을 위해 터미널의 내용을 잠시 숨김



## 깃 명령어 정리

0. `git status` : 현재상황을 알아볼 수 있다

1. `git init` : 특정 폴더를 깃으로 관리하겠다

   => ★중요 : 홈폴더에서는 이 명령어를 사용하지않는다. ★

2. `git add 올릴파일명.확장자` : 파일을 Staging Area에 올린다

   `git add .` : 현재 폴더의 모든 파일을 Staging Area에 올린다

3. `git commit -m '커밋메세지'` : 파일을 사진 찍어 사진 저장소에 보관한다. (커밋메세지는 사진의 인덱스)

4. `git log` 또는 `git log --oneline` : 제대로 되었는지 확인



* 파일명 옆에 뜬 영문자의 의미
  * `U` : Untracked 깃에게 언택트되고 있음
  * `M` : 파일을 수정했음  - > 수정을 했으면 `ctrl+s`를 통해 저장해야한다.

* 전 버전을 보려면
  * `git checkout head~(숫자)`	: (숫자)번째 버전 보기
  * `git checkout 해쉬값`	: 해쉬값에 해당하는 버전 보기
  * 돌아오려면 `git checkout master` 입력
