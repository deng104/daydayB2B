from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from user.models import User
import re


# Create your views here.

def register(request):
    """注册页面"""
    if request.method == 'POST':
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        # 进行数据校验
        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})
        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})
        # 校验用户名是否重复
        user = User.objects.filter(username=username)
        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})
        # 进行业务处理： 进行用户注册
        user = User.objects.create_user(username, password, email)
        user.is_active = 0
        user.save()
        # 返回应答
        return redirect(reverse('goods:index'))
    return render(request, 'register.html')


def register_handle(request):
    """进行注册处理"""
    pass


class RegisterView(View):
    """注册"""
    def get(self, request):
        # 显示注册页面
        return render(request, 'register.html')
    
    def post(self, request):
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        if not all([username, password, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2, 5}){1, 2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
        if allow != 'on':
            return request(request, 'register.html', {'errmsg': '请同意协议'})
        user = User.objects.filter(username=username)
        if user:
            return request(render, 'register.html', {'errmsg': '用户名已存在'})
        
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()
        return 
            
            
            
    