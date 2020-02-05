from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from base import models as m_base


def explain(request):
    return HttpResponse('基础页面，平台主页等')


def login(request):
    return render(request,'index.html')


def login_do(request):
    account = request.POST.get('account')
    password = request.POST.get('password')
    try:
        user_obj = m_base.Users.objects.get(account=account,password=password)
    except m_base.models.ObjectDoesNotExist:
        return render(request,'index.html',{'info':'账号或密码错误'})
    request.session['user_id']=user_obj.id
    request.session['user_name']=user_obj.name
    print(user_obj.role)
    #print(request.session)
    if user_obj.email==None:
        return render(request,'yjbd.html')
    if user_obj.role=='普通用户':
        #return HttpResponse('用户登录成功')
        return render(request,'main.html')
    elif user_obj.role=='管理员':
        return render(request,'main.html')


def bind_email(request):
    return render(request, 'yjbd.html')
