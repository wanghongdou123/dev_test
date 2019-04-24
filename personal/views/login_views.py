from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from personal.models.project import Project


# Create your views here.
def say_hello(request):
    input_name = request.GET.get("name","")
    if input_name == "":
        # return HttpResponse(talk)
        pass
    return render(request, "index.html", {"name":input_name})


def index(request):
    """
    登录的首页
    """
    if request.method == 'GET':
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = auth.authenticate(
            username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)  # 验证登录
            return HttpResponseRedirect('/project/')
        else:
            return render(request, "index.html",
                          {"error": "用户名或者密码错误"})


# 数据库 -- 》user表  --》通过pymysql这个驱动链接mysql


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')





