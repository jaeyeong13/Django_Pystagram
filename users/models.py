from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
  '''
  AbstractUser는 Django가 CustomUser 모델을 만들기 위해 제공하는 기본 유저 형태를 가진 모델 클래스이다.
  이 클래스는 Django의 기본 User모델이 가진 필드를 똑같이 가지고 있으며, AbstractUser를 상속받으면 자동적으로 username, password, first_name, last_name, email, is_staff(관리자 여부), is_active(활성화 여부), date_joined, last_login 필드들이 모델에 추가된다.
  '''
  profile_image = models.ImageField(
    '프로필 이미지', upload_to='users/profile', blank=True
  )
  short_description = models.TextField('소개글', blank=True)   # 여기까지 하고, 모델을 변경했으므로 변경사항에 대한 migration을 생성하고 적용한다.