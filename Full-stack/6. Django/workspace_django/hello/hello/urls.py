"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hello01/', include('hello01.urls'))
]
# path('', views.index) : 클라이언트에서 서브로 아무것도 없는 요청(기본요청)이 들어오면 views.index에 있는 함수로 가라.
# 이 인덱스라는 함수는 요청 받아서 HttpResponse해서 반환해라. 그래서 브라우저는 이걸 받아서 예쁘게 출력한다.

# 요청이 들어왔는데 서버에 앱을 여러개 만들어놔서 원래는 요청들어온거에서 여러개를 다 연결하는데, 각 열마다 urls.py를 따로 만들어서 알아서 연결하도록 함