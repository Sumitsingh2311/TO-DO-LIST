from django.shortcuts import render , redirect
from . forms import Hello
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.

def register(request):
    form = Hello()
    if request.method == 'POST':
        form = Hello(request.POST)
        if form.is_valid():
            form.save()
            # print('sucesss')
    context = {
        'form': form
    }
    return render(request,'register.html',context)


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pass')

        user = authenticate(request,username = username, password = password)

        if user is not None:

            login(request , user)
            return redirect('app/main')
        else:
            messages.error(request,'Invalid user name and pasword')
            return render(request,'login.html')

            
    return render(request,'login.html')


def log_out(request):
    logout(request)
    return redirect('log_in')