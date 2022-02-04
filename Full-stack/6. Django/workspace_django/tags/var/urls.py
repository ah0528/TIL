from django.urls import path
from . import views

# <a href="{% url 'index' %}">go index</a>
# : name이 index인 것을 찾아라!

urlpatterns = [
    path('', views.index, name='index'), # name='index': 이 경로에 이름을 index라고 붙임
    path('var01/', views.variables01),
    path('var02/', views.variables02),
    path('forloop/', views.for_loop),
    path('if01/', views.if01),
    path('if02/', views.if02),
    path('href/', views.href),
    path('request/', views.get_post),
]