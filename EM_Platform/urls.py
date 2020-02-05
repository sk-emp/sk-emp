"""EM_Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views as v_base
from borrow import views as v_borrow
from equipment import views as v_equipment
from approval import views as v_approval
from notice import views as v_notice

urlpatterns = [
    path('base',v_base.explain),
    path('borrow',v_borrow.explain),
    path('equipment',v_equipment.explain),
    path('approval',v_approval.explain),
    path('notice',v_notice.explain),
    path('admin/', admin.site.urls),
    ##########
    path('login',v_base.login,name='login'),
    path('login_do',v_base.login_do,name='login_do'),
    path('bind_email',v_base.bind_email,name='bind_email'),
    path('send_vc_email',v_notice.send_VCode_email,name='send_vc')
]
