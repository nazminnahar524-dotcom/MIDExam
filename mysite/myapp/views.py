from django.shortcuts import render, redirect

from mysite.myapp.forms import LaptopForm


# Create your views here.
def list(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else :
        form = LaptopForm()
    return render(request,'list.html',context={'form':form})