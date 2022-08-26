from unittest import result
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
     return render(request,'home.html',{'name':'Abhi'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1*val2
    return render(request,'result.html',{'result':res})