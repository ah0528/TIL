# WEB

HTTP를 통해 client의 **요청**과 그 요청에 대해 알맞는 데이터(document)를 **응답**하는 server

- HTTP(HyperText Transfer Protocol) : client와 server 사이의 통신 규약

## Web의 개념

* WWW(World Wide Web)을 일반적으로 웹(web)이라고 부름

* 웹은 각종 형태의 텍스트, 그림, 동영상, 음악 등 데이터를 교환하기 위한 종합 데이터베이스
* 클라이언트와 서버 구조로 이루어짐
  * 분산 하이퍼텍스트 시스템
  * 실시간 쌍방향
  * 시공간에 제약 없음
* 클라이언트(client)
  * HTTP 통신규약으로 웹서버와 접속하는 웹 브라우저 프로그램
  * URL을 해석해 웹 서버에 접속해서 데이터(document)를 요청하고, 서버로부터 받은 데이터를 보여줌
* 서버(server)
  * HTTP 프로토콜을 이용하여 클라이언트의 요청에 응답함
  * 서버에는 다양한 자원이 저장되어 있으나 전송되는 것은 HTML 형태의 문서나 이미지이고, HTML 형식이 아닌 정보는 서버측 응용 프로그램을 사용하여 HTML형식으로 바꿔서 전송함
* 웹의 작동원리 : 클라이언트가 요청한 문서를 서버가 클라이언트에 송신하고, 클라이언트는 해당 문서를 받음



## Web의 전송방식

* TCP/IP 통신 프로토콜
  * 인터넷에서 컴퓨터 간의 데이터 송수신을 위한 통신규약
  * TCP (Transmission Control Protocol) : 데이터의 흐름을 제어하고 데이터가 정확한지 확인
  * IP (Internet Protocol) : 이동하는 데이터의 목적지를 지정하는 역할
  * 통신 프로토콜 : 컴퓨터간의 통신 규약



* HTTP(HyperText Transfer Protocol) 프로토콜
  * 웹 문서를 위한 통신규약
  * 클라이언트와 서버 사이에 하이퍼텍스트 문서를 위한 통신규약
  * 요구(request)와 응답(response)형식으로 되어 있음



* FTP(File Transfer Protocol)
  * 인터넷을 통해 대량의 파일을 전송하기 위한 통신 규약



## 주소체계

* 도메인 주소 (Domain Name)

IP 주소는 숫자로 구성되어 있어 이용하기 불편해 쉽게 기억할 수 있도록 문자로 대채한 것



* URL (Uniform Resource Locator)

웹에서 각종 파일 들 자원의 위치를 표시하는 표준
`프로토콜://호스트주소[:포트번호]/파일경로`

