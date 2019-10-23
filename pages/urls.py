from django.contrib import admin
from django.urls import path
from . import views #自分で作ったviews.pyを読み込むために必要


urlpatterns = [
    path('', views.toppage, name='toppage'),
]