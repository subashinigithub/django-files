from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new1(req):
    return HttpResponse("this is first page")

def new2(req):
    return HttpResponse("this is second page")