"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from config.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),       # 관리자 페이지
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),  # users/urls.py를 추가
    path('', index),    # 경로가 없을 때 index View 연결
]
urlpatterns += static(      # 사용자가 업로드한 정적파일
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
