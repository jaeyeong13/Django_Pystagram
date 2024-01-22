from django.shortcuts import render, redirect
from posts.models import Post

# Create your views here.
def feeds(request):
  if not request.user.is_authenticated:
    # 사용자가 로그인하지 않은 경우, 로그인 페이지로 이동시킴
    return redirect('/users/login/')
  posts = Post.objects.all()
  context = {'posts': posts}
  return render(request, 'posts/feeds.html', context)