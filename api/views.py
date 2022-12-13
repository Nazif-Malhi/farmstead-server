from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import tensorflow as tf


def page(request):
    print('runing yes')
    print(tf.__version__)
    return HttpResponse("Hello World tf ---> version" + tf.__version__)
