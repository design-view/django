from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def main(request):
    return render(request, 'main/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 변수에 Post테이블에 있는 행을 담아줌
    posts = Post.objects.all()
    # view로 데이터를 전달 
    return render(request, 'main/blog.html', {'postlist': posts})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                contents = request.POST['contents'],
                mainphoto = request.POST['mainphoto']
            )
        else:
            new_article = Post.objects.create(
                postname = request.POST['postname'],
                contents = request.POST['contents'],
            )
        # urls.py파일에 있는 주소를 실행하는 기능 
        return redirect('/blog/')
    return render(request,'main/new_post.html')

def remove_post(request, pk):
    #데이터베이스 에서 삭제할 행을 변수에 저장
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        # 삭제 
        post.delete()
        return redirect('/blog/')
    # get일때는 그냥 페이지 보여줌 
    return render(request, 'main/remove_post.html',{'Post':post})