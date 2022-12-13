from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def page(request):
    print('runing')
    return HttpResponse("Hello World")
