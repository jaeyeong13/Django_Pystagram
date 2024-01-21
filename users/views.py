from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import LoginForm

# Create your views here.
def login_view(request):
  # 이미 로그인되어 있다면 피드 페이지로 이동시킴
  if request.user.is_authenticated:
    return redirect('/posts/feeds/')

  if request.method == 'POST':
    form = LoginForm(data = request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username = username, password = password)

      if user:
        login(request, user)
        return redirect('/posts/feeds/')
      else:
        print('로그인에 실패했습니다.')
    context = {'form': form}
    return render(request, 'users/login.html', context)
  else:
    form = LoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)
