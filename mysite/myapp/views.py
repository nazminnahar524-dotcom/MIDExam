from django.shortcuts import render, redirect, get_object_or_404

from .forms import LaptopForm
from .models import Laptop


# Create your views here.
def list(request):
    laptop = Laptop.objects.all()
    return render(request,'list.html',context={'laptop':laptop})

def create(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else :
        form = LaptopForm()
    return render(request,'create.html',context={'form':form})

def edit(request,id):
    laptop = get_object_or_404(Laptop,id=id)
    if request.method == "POST":
        form = LaptopForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('/')

    else :
        form = LaptopForm(instance=laptop)
    return render(request,'edit.html',context={'form':form})

def delete(request,id):
    laptop = get_object_or_404(Laptop, id=id)
    if request.method == "POST":
        laptop.delete()
        return redirect('/')

    return render(request, 'delete.html')