from django.db import models

# Create your models here.
ROLE=(
    ('管理员','管理员'),
    ('普通用户','普通用户'),
)

class Users(models.Model):
    name = models.CharField('姓名',max_length=40)
    account = models.CharField('用户名',max_length=40)
    password = models.CharField('密码',max_length=20)
    role = models.CharField('角色',choices=ROLE,default='普通用户')