#### 가상환경

특정 버전의 특전 모듈을 사용하는 파이썬을 사용하고 싶다면 가상환경을 사용하면 됨.

1. virtual environments (venv) 모듈로 생성하기

   - 가상환경 생성하기

   python -m venv ??(가상환경 이름)

   - venv 실행

   windows의 경우, 

   .\??\Scripts\activate.bat

   mac의 경우, 

   source ??/bin/activate

   

2.  conda 가상환경

   conda create -n myweb python=3.9

   conda activate myweb

   conda info --envs			확인하기



Django 설치하기



pip install django

cd /workspaces/workspace_django

django-admin startproject mysite				mysite라는 이름의 장고 프로젝트 만듦



cd mysite

python manage.py runserver						서버 실행



django -admin startproject hello					폴더 hello 생성



단축키 alt + 1 : 메뉴창 여닫기

alt + insert : 새로운 폴더 만들기



hello/hello/views.py



cd hello

python manage.py runserver



localhost:8000/로 요청이 들어간 것



python manage.py startapp hello01    project(네이버) 속 app(메일, 카페, 블로그 등등)



render

SSR (server sending rendering) : 서버에서 그려줄거야

CSR(client sending rendering) : 클라이언트에서 그려줄거야

장고는 SSR, 즉 요청이 들어오면 그 요청을 urls.py로 가고 view에서 처리하고 서버에서 만들고 응답해줌



hello/hello01/urls.py