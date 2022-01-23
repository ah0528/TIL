css



스타일시트 작성 방법

1. 인라인 요소로 작성

` <b style="color:red">1. 인라인 스타일</b>`

1. 내부 스타일

`<head> 부분에 <style>태그 안에 작성`

`

<style>

​    p{

​      background-color: coral;

​    }

  </style>`

1.  외부 스타일

`<link rel="stylesheet" href="resources/css/css01.css" type="text/css"/>`

link 태그를 이용해 외부 스타일시트를 불러오도록 수정





* css에서 태그와 태그 사이에 여백을 나타내는 margin 이라는 속성이 있습니다. 여기서는 두 번째 <p>태그에 위쪽 여백을 주고 싶은상태이므로 'margin-top:40px'이란 코드를 사용할 수 있습니다.
* 언스플래시(http://unsplash.com/) 고품질 이미지 저작권 구애없음
* 이미지 넣기 `<img src="이미지 주소" wwidth="원하는 크기">`
* `<meta charset="utf-8">`





* 앵커 태그

  * 하이퍼링크 설정

    * 1. 특정 웹 페이지에 연결하기

      `<a href="http://www.naver.com">네이버</a>`

    * 2. 웹페이지 내부에 연결하기

      `<a href="#alpha">Alpha로 이동</a>`

      `<p id="alpha">hi~~~!!!</p>`





css 폰트를 한 줄로 작성하는 방법

h1{font-weight:blod;}



footer nav.fnb{text-align:center;height:40px;word-break : nowrap;display : inline-block; text-overflow : clip;

overflow : hidden; white-space : nowrap; }