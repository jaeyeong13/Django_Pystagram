from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
  # 이미 로그인되어 있다면 피드 페이지로 이동시킴
  if request.user.is_authenticated:
    return redirect('/posts/feeds/')
  return render(request, 'users/login.html')
