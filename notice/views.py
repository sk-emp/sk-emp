from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def explain(request):
    return HttpResponse('消息推送模块')