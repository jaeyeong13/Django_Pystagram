# app별로 urls.py 파일의 내용을 분리한다.
from django.urls import path
from users.views import login_view

urlpatterns = [
  path('login/', login_view),
]
