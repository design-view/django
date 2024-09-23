from django.shortcuts import redirect, render

from .models import Notice

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def notice(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    noticelist = Notice.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'main/notice_list.html', {'noticeList':noticelist})

def noticeView(request,pk):
   notice = Notice.objects.get(pk=pk)
   return render(request, 'main/notice_view.html', {'notice':notice})

#삭제하기
def notice_remove(request,pk):  
    print(pk)
    notice = Notice.objects.get(pk=pk)
    if request.method == 'POST':    
        # 삭제 
        notice.delete()
    return redirect('/notice')
#추가하기
def notice_add(request):
    if request.method == 'POST':
        new_notice = Notice.objects.create(
            title = request.POST['title'],
            contents = request.POST['contents'],
            views = 0,
        )
        # urls.py파일에 있는 주소를 실행하는 기능 
        return redirect('/notice')
    return render(request,'main/notice_add.html')