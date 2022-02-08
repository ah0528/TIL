from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('var01/', views.variables01),
]