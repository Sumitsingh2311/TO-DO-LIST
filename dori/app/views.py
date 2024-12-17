from django.shortcuts import render, redirect
from .models import List, Deleted
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def show(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        descp = request.POST.get('desc')
        # print(title,descp)
        san = List.objects.create(title = title,desc = descp)
        return  redirect('display')
        
    return render(request,'home.html')


@login_required(login_url='login')
def display(request):
    dis = List.objects.all().order_by('-id')
    context = {
        'dis' : dis
    }
    return render(request,'display.html',context)


@login_required(login_url='login')
def details(request,pk):
    # pk = 2
    dis = List.objects.get(id = pk)
    if request.method == 'POST':
        Deleted.objects.create(title = dis.title, desc = dis.desc)
        dis.delete()
        return redirect('history')

    context = {
        'dis' :dis
    }

    return render(request,'details.html',context)


@login_required(login_url='login')
def edit(request,pk):
    edit = List.objects.get(id = pk)
    if request.method == 'POST':
        edit.title = request.POST.get('title')
        edit.desc = request.POST.get('desc')
        edit.save()
        return redirect('display')

    context = {
        'edit':edit
    }
        
    return render(request,'edit.html',context)


@login_required(login_url='login')
def history(request):

    dele = Deleted.objects.all()

    if  request.method =='POST':
        dele.delete()

    context = {
        'dele' : dele
    }

    return render(request,'history.html',context)

