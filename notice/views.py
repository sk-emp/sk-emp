from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from EM_Platform import settings


def explain(request):
    return HttpResponse('消息推送模块')

def send_VCode_email(request):
    if request.method=='POST':
        goal_email = request.POST.get('email')
        v_code = 'ae86'
        res = send_mail('设备管理平台邮箱绑定验证',
                        '您在设备管理平台申请绑定该邮箱，验证码为:'+v_code+'，若非本人操作请忽略此邮件',
                        settings.DEFAULT_FROM_EMAIL,
                        ['sk_emp@163.com'])
        if res==1:
            return render(request, 'yjbd.html',{'info':'验证码发送成功'})
        else:
            return render(request, 'yjbd.html',{'info':'验证码发送失败，请重试'})
    else:
        return render(request,'yjbd.html')
