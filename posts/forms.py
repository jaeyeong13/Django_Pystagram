from django import forms
from posts.models import Comment

class CommentForm(forms.ModelForm):   # ModelForm 클래스 - Form클래스와 유사하나, DB 테이블에 해당하는 "모델 클래스"와 연관된 기능들을 제공한다.
  class Meta:
    model = Comment
    fields = [
      'post',
      'content',
    ]
    widgets = {
      'content': forms.Textarea(
        attrs={
          'placeholder': '댓글 달기...',
        }
      )
    }
