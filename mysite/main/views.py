from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    #templates폴더 안에있는 폴더 및 html파일의 경로를 설정
    return render(request,'main/index.html')

def notice(request):
    noticelist = Notice.objects.all()
    return render(request,'main/notice_list.html', {'noticeList':noticelist})

def notice_view(request,pk):
    notice = Notice.objects.get(pk=pk)
    return render(request, 'main/notice_view.html', {'notice':notice})

def notice_add(request):
    if request.method == 'POST':
        new_notice = Notice.objects.create(
            title = request.POST['title'],
            contents = request.POST['contents'],
            views = 0,
        )
        return redirect('/notice/')
    return render(request, 'main/notice_add.html')

def notice_remove(request,pk):
    if request.method == 'POST':
        notice = Notice.objects.get(pk=pk)
        notice.delete()
    return redirect('/notice/')
