from django.shortcuts import render
from .forms import Using
# Create your views here.

def register(request):
    form = Using() 
    if request.method == 'POST':
        form =Using(request.POST)
        if form.is_valid():
            form.save()
            print('success')

    context = {
        'form':form
    }
    return render(request,'register.html',context)