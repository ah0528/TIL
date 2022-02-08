# Django에 외부 css, 외부 javascript를 사용한다면

# 1. 해당 project나 app에 templates 폴더를 만든다.
# 2. templates 파일 속에 project 또는 app의 이름과 같은 폴더를 만든다.
# 3. 그 폴더 속에 html파일을 만든다.

# html 파일에서 외부 css와 외부 javascript 사용하기
<html>
<head>
    {% load 외부파일이 들어있는 파일명 %}
    <link rel= "stylesheet" href="{% css파일이 들어있는 파일명 'css파일명.css' %}">
    <script src="{% js가 들어있는 파일명 'js파일명.js' %}"></script>
</head>

<body>
</body>
</html>

# 그리고 views.py에서 로직을 구현해야함
# render 함수를 사용하기 위해 from django.shortcuts import render를 해줘야함
from django.shortcuts import render

def index(request):
    return render(request, 'templates폴더에서 html이 들어있는 폴더명/html명')