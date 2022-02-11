from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone
from django.core.paginator import Paginator

def index(request):
    myboard = MyBoard.objects.all().order_by('-id')
    paginator = Paginator(myboard, '5')
    page_num = request.GET.get('page', '1')

    page_obj = paginator.get_page(page_num)

    return render(request, 'index.html', {'list': page_obj})

def insert_form(request):
    return render(request, 'insert.html')

def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())
    if result:
        return redirect('index')
    else:
        return redirect('insertform')

def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})

def update_form(request, id):
    return render(request, 'update.html', {'dto':MyBoard.objects.get(id=id)})

def update_res(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)
    result_mytitle = myboard.update(mytitle=mytitle)
    result_mycontent = myboard.update(mycontent=mycontent)

    if result_mytitle + result_mycontent == 2:
        return redirect('/detail/'+id)
    else:
        return redirect('/updateform/'+id)

def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()
    if result_delete[0]:
        return redirect('/')
    else:
        return redirect('/detail/'+id)