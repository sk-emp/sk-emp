from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def explain(request):
    return HttpResponse('基础页面，平台主页等')