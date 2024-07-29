from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.
def nxt(r):
    return HttpResponse("new one")
def nif(r):
    return HttpResponse("this is new 1")
def page2(r):
    return render(r,"index.html",name='home')
def page3(r):
    return render(r, "new.html")
from .forms import *
""" def department_form(request):
    if request.method=='POST':
        form=Itemforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Itemforms()
    return render(request,'form.html',{'form':form}) """
def student_form(request):
    if request.method=='POST':
        form=Itemforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=Itemforms()
        return render(request,'form.html',{'form':form})
