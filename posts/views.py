from django.shortcuts import render, redirect
from posts.models import Post, Comment
from posts.forms import CommentForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden

# Create your views here.
def feeds(request):
  if not request.user.is_authenticated:
    # 사용자가 로그인하지 않은 경우, 로그인 페이지로 이동시킴
    return redirect('/users/login/')
  posts = Post.objects.all()
  comment_form = CommentForm()
  context = {
    'posts': posts,
    'comment_form': comment_form,
  }
  return render(request, 'posts/feeds.html', context)


@require_POST   # 댓글 작성을 처리할 View, Post 요청만 허용한다.
def comment_add(request):
  form = CommentForm(data=request.POST)
  if form.is_valid():
    comment = form.save(commit=False)   # commit = False 옵션으로 메모리상에 Comment 객체 생성
    comment.user = request.user   # Comment 생성에 필요한 사용자 정보를 request에서 가져와 할당
    comment.save()    # DB에 Comment 객체 저장
    print(comment.id)
    print(comment.content)
    print(comment.user)
    return HttpResponseRedirect(f'/posts/feeds/#post-{comment.post.id}')    # 생성 완료 후에는 피드 페이지로 다시 이동


@require_POST
def comment_delete(request, comment_id):
  if request.method == 'POST':
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
      comment.delete()
      return HttpResponseRedirect(f'/posts/feeds/#post-{comment.post.id}')
    else:
      return HttpResponseForbidden('이 댓글을 삭제할 권한이 없습니다.')
