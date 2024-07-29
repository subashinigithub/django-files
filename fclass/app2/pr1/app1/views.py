from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
def new1(r):
    return  HttpResponse("ytgffv")
def add(req):
    return  HttpResponse("Welcome to our site")
def sub(req):
    a=10
    b=12
    c=a+b
    return HttpResponse(c)
def multi(r):
    return HttpResponse("Hello world")
def nxt(r):
    return HttpResponse("new one")
def align(r):
    return HttpResponse("call again",name='home')
from .forms import *
def department_form(request):
    if request.method=='POST':
        form=Itemforms(request.Post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Itemforms()
    return render(request,'form.html',{'form':form})