from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apptest.models import Appcase,Appcasestep
# Create your views here.

# app 用例管理
@login_required

def appcase_manage(request):
    appcase_list = Appcase.objects.all()
    uesrname = request.session.get('user','') #读取浏览器登录 session
    return render(request,'appcase_manage.html',{'user':uesrname,'appcases':appcase_list})

#app 用例测试步骤
@login_required

def appcasestep_manage(request):
    uesrname = request.session.get('user','')
    appcasestep_list = Appcasestep.objects.all()
    return render(request,'appcasestep_manage.html',{'user':uesrname,'appcasesteps':appcasestep_list})


