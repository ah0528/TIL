0209 crawling



가상환경 만들기

CMD창에 conda create -n mycrawling python==3.9

파이참 New project

Location을 만들어 준 workspace_crawling으로 지정

Previously configured interpreter의 Interpreter의 ...선택 후 Conda Environment에 Interpreter에 anaconda3\envs\mycrawling\python.exe 지정 후 OK -> create



Terminal창 pip install beautifulsoup4



beautifulsoup4 홈페이지

[Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

parser : 문자열로 되어있는 것을 객체화

parse tree :



| Parser               | Typical usage                          | Advantages                                               | Disadvantages                                    |
| -------------------- | -------------------------------------- | -------------------------------------------------------- | ------------------------------------------------ |
| Python’s html.parser | `BeautifulSoup(markup, "html.parser")` | Batteries includedDecent speedLenient (As of Python 3.2) | Not as fast as lxml, less lenient than html5lib. |

우리는 위의 이걸 사용할거야



```
from bs4 import BeautifulSoup
```







<우리가 할 일!>

https://movie.naver.com/movie/running/current.naver에서 상영작예정작의

영화제목과 평점을 자동으로 가져올 것



크롤링 : 해당 내용을 다 가져옴

스크랩핑 : 필요한 내용을 골라 가져옴



파이참 naver/movies.py 생성

```
from bs4 import BeautifulSoup
import urllib.request
```

import urllib.request : 클라이언트 역할을 함

urllib.request : 요청하는 것을 사용할거야. (서버에게 뭔가 요청을 함)

urllib.request.urlopen('url주소') : 도큐먼트가 들어있음, 문서를 객체형식으로 받아옴

response에 들어있는 건 document임. 문자열로 응답된 도큐먼트를 클라이언트(브라우저)가 예쁘게 그려줌



```
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```

이 문자열을 객체화. (js의 DOM과 비슷)



```
soup = BeautifulSoup(resp, 'html.parser')
print(type(soup))
```

'html.parser' : 파이썬의 내장 parser를 이용해서 parse tree를 만들어줌.

노드 구조를 BeautifulSoup이 만들어줌.

soup = <class 'bs4.BeautifulSoup'> = 객체



개발자도구 들어가서 원하는 부분을 찾기

제목은 a태그 안에 텍스트로 들어가 있음

별점은 span태그 안에 텍스트로 들어가있음



## `find_all()`

Method signature: find_all([name](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#id12), [attrs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#attrs), [recursive](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#recursive), [string](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#id13), [limit](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#limit), [**kwargs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kwargs))

The `find_all()` method looks through a tag’s descendants and retrieves all descendants that match your filters. I gave several examples in [Kinds of filters](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters), but here are a few more:

```
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
soup.find(string=re.compile("sisters"))
# 'Once upon a time there were three little sisters; and their names were\n'
```

Some of these should look familiar, but others are new. What does it mean to pass in a value for `string`, or `id`? Why does `find_all("p", "title")` find a <p> tag with the CSS class “title”? Let’s look at the arguments to `find_all()`.



dl태그로 뭉텅이 잡혀있는거 안에 제목과 별점이 있음



findAll보다 find_all이 더 최근 메소드



제목 가져오기

Find tags by attribute value:

```
soup.select('a[href="http://example.com/elsie"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select('a[href^="http://example.com/"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select('a[href$="tillie"]')
# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select('a[href*=".com/el"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```

There’s also a method called `select_one()`, which finds only the first tag that matches a selector:

```
soup.select_one(".sister")
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
```



## `find()`

Method signature: find([name](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#id12), [attrs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#attrs), [recursive](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#recursive), [string](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#id13), [**kwargs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kwargs))

The `find_all()` method scans the entire document looking for results, but sometimes you only want to find one result. If you know a document only has one <body> tag, it’s a waste of time to scan the entire document looking for more. Rather than passing in `limit=1` every time you call `find_all`, you can use the `find()` method. These two lines of code are nearly equivalent:

```
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>
```

The only difference is that `find_all()` returns a list containing the single result, and `find()` just returns the result.

If `find_all()` can’t find anything, it returns an empty list. If `find()` can’t find anything, it returns `None`:

```
print(soup.find("nosuchtag"))
# None
```

Remember the `soup.head.title` trick from [Navigating using tag names](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-using-tag-names)? That trick works by repeatedly calling `find()`:

```
soup.head.title
# <title>The Dormouse's story</title>

soup.find("head").find("title")
# <title>The Dormouse's story</title>
```





<네이버 수요웹툰 

naver/webtoons.py 생성

터미널 창에 pip install requests

```
# -*- coding:utf-8 -*-
```

 : 해당 파이썬 파일은 utf-8로 인코딩 됨 (주석 안에 써야 적용됨)



```
from bs4 import BeautifulSoup
import requests
import json
```

requests 모듈은 누군가 만든 것

urllkib.request은 파이썬이 만든 것

둘의 기능은 같음



```
url='https://comic.naver.com/webtoon/weekdayList?week=wed'
resp = requests.get(url)
```

url을 get방식으로 가져와 requests하겠다.

```
print(resp)
print(resp.text)
```

print(resp) 하면 `<Reaponse [200]>` : requests의 객체는 response라는 객체를 만들고, html 응답코드를 작성해서 반환

print(resp.text) 하면 문자열을 반환





```
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)
```



전체 필요로하는 얘들 덩어리를 가져오고, 반복해서 원하는 얘들만 뽑아오기

ul class=

dl태그 안의 dt안의 title과 dd안의 span안의 strong 태그의 별점을 가져오면 됨



```
webtoons = soup.find('ul', {'class': 'img_list'})
```

soup.find('ul', class_='img_list') 와 같음



```
for dl in dl_list:
    title = dl.find('a')['title']
    star = dl.find('strong').text
```

dl에서 a태그를 찾고, title을 가져와 변수 title에 저장

['title'] : 해당 태그의 속성값 가져와주세요

dl에서 strong태그 찾고 text값 가져와 star에 저장









naver.com/robots.txt 해서 저장된 txt파일 열어보면 이렇게 적혀있음 : 해당사이트에 허용한다/ 금한다

User-agent: *			-> 여기에 적힌 봇의 권한
Disallow: /			 	-> 루트부터 다 금지
Allow : /$ 				  -> 첫 시작화면만 허용

주소 뒤에 robots.txt를 쳐서 크롤링할때는 잘 확인해보고 해야함.



공공데이터 포털은

```
User-agent: *
#DaumWebMasterTool:4978f9b94e10dbe5672e5aab80f8868382a8d6b2319a391dc7904bd20ced54f9:mgC7BXBG6UtCrUlKPK7+eA==
```

다 된다~!

open api site이기 때문에.

api : 원하는 형태에 맞춰서 요청을 하면 응답해줌

open api : 클라이언트가 서버의 양식에 맞게 요청하면 데이터 공유









공공데이터 포털> 데이터목록 : 교육> 파일데이터> 1페이지~10페이지 자료의 제목가져오기



해당 페이지 링크의 &currentPage=숫자 숫자에 원하는 페이지 숫자를 넣으면 해당 페이지로 요청함

https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5   만 넣어서 요청해도 페이지 잘 나옴(값없는 부분 지움)









공공데이터 포털 코로나 자료

마이페이지 > 자료 제목 > 개발계정 상세보기의 End Point

End Point	http://openapi.data.go.kr/openapi/service/rest/Covid19

이게 이 자료의 url, 서비스 전체를 관리하는 것. (코로나 자료들 전체)



참고문서의 docx파일 다운> 3페이지

http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=인증키(URL Encode) pageNo=1&numOfRows=10&startCreateDt=20200410&endCreateDt=20200410



개발자계정 상세보기의 일반인증키(Encoding)를 파이참에 붙여넣기

```
service_key = '9vOfwJR3In%2FUxXZ08mFwxKcx9dWQu32uESbwSMVax8Qi1BXKCup6lkjb79VVlST4rJaVGeHuyCogERk9qaezLg%3D%3D'
```



개발계정 상세보기의 기본정보의 데이터명의 상세설명 > 서비스URL을 url = ''에 넣어주거나

서비스URL 뒷부분인 `getCovid19SidoInfStateJson`을 End Point 주소의 뒤에 붙임

url = '`End Point`+`getCovid19SidoInfStateJson`' 

```
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'
```





<item>

<createDt>2022-02-09 10:38:16.257</createDt>

<deathCnt>6943</deathCnt>

<defCnt>1131239</defCnt>

<gubun>합계</gubun>

<gubunCn>合计</gubunCn>

<gubunEn>Total</gubunEn>

<incDec>49567</incDec>

<isolClearCnt>719627</isolClearCnt>

<localOccCnt>49402</localOccCnt>

<overFlowCnt>165</overFlowCnt>

<qurRate>2191</qurRate>

<seq>15001</seq>

<stdDay>2022년 02월 09일 00시</stdDay>

<updateDt>null</updateDt>

</item>



합계라는 글을 찾아서 49567, 49402, 165, 2022년 02월 09일 00시를 가져오고싶음















인스타그램

react.js는 CSR(client에서 화면을 rendering(그려줄거야))일듯... 그래서 selenium을 사용하자 !

https://www.selenium.dev/

selenium은 브라우저를 자동화합니다.

자동화하고 싶을 때 셀레니움 사용하면 됨

```python
from selenium import webdriver
```

웹 드라이버가 자동으로 클릭해주고, 넘겨주고 등등 해줌

https://www.selenium.dev/documentation/webdriver/



구글에 webdriver 검색 > [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/)

드라이브 다운로드하고 파이참에 drivers폴더 안에 압축 풀어 exe 넣어주기

터미널에 pip install selenium

```
service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
```

크롬 드라이버 사용할거야







X-path : tree형 절대경로

