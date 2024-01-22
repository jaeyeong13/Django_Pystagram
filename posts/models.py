from django.db import models

# Create your models here.

class Post(models.Model):
    # 'users.User' 모델을 참조하는 외래 키. Post는 특정 User에 속함.
    user = models.ForeignKey(
        'users.User',
        verbose_name='작성자',
        on_delete=models.CASCADE,   # 연관된 User가 삭제될 경우 해당 User의 모든 Post도 삭제됨을 의미.
    )
    # 포스트의 내용을 나타내는 텍스트 필드
    content = models.TextField('내용')
    # 포스트가 생성된 날짜 및 시간을 저장. 'auto_now_add=True'는 객체가 처음 생성될 때의 시간을 자동으로 설정.
    created = models.DateTimeField('작성일시', auto_now_add=True)


class PostImage(models.Model):
    # 'Post' 모델을 참조하는 외래 키. PostImage는 특정 Post에 속함.
    post = models.ForeignKey(
        Post,
        verbose_name='포스트',
        on_delete=models.CASCADE,   # 연관된 Post가 삭제될 경우 해당 Post의 모든 이미지도 삭제됨을 의미.
    )
    photo = models.ImageField('사진', upload_to='post')   # 이미지 파일을 저장하는 필드. 'upload_to'는 업로드된 파일이 저장될 경로를 설정.



class Comment(models.Model):
    # 'users.User' 모델을 참조하는 외래 키. Comment는 특정 User에 속함.
    user = models.ForeignKey(
        'users.User',
        verbose_name='작성자',
        on_delete=models.CASCADE,
    )
    # 'Post' 모델을 참조하는 외래 키. Comment는 특정 Post에 속함.
    post = models.ForeignKey(Post, verbose_name='포스트', on_delete=models.CASCADE)
    content = models.TextField('내용')
    created = models.DateTimeField('작성일시', auto_now_add=True)
