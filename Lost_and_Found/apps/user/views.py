from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.views.generic import View
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.contrib.auth import authenticate, login, logout
from utils.Mixin import LoginRequiredMixin

from email.mime.text import MIMEText
import smtplib
from email.header import Header  # 设置编码方式
import re,random,json
from urllib import parse
from urllib import request as req

# Create your views here.

def index(request):
    items = Item.objects.all()
    types = Type.objects.all()
    try:
        openid = request.session['openid']  # 读取Session
        user = User.objects.get(openid=openid)  # 根据Session获取用户信息
        return render(request, 'index.html', {'user': user, 'item_types': types, 'items': items})
    except:  # 如果发生异常
        user_id = request.COOKIES.get('user_id')
        if user_id:
            user = User.objects.get(user_id=user_id)
            return render(request, 'index.html', {'user':user,'item_types': types, 'items': items})
        else:
            return render(request,'index.html',{'item_types': types, 'items': items})


def to_login(request):
    state = str(random.randrange(100000, 999999))  # 定义一个随机状态码，防止跨域伪造攻击。
    request.session['state'] = state  # 将随机状态码存入Session，用于授权信息返回时验证。
    client_id = '101525456'  # QQ互联中网站应用的APP ID。
    callback = parse.urlencode({'redirect_uri': 'http://127.0.0.1:8000/user/signup'})
    # 对回调地址进行编码，用户同意授权后将调用此链接。
    login_url = 'https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=%s&%s&state=%s' % (
        client_id, callback, state)  # 组织QQ第三方登录链接
    return HttpResponseRedirect(login_url)  # 重定向到QQ第三方登录授权页面


def QQ_login(request):
    if request.session['state'] == request.GET['state']:  # 验证状态码，防止跨域伪造攻击。
        code = request.GET['code']  # 获取用户授权码
        client_id = '101525456'  # QQ互联中网站应用的APP ID。
        client_secret = 'a626c27aaecbf09c596722e91b231e52'  # QQ互联中网站应用的APP Key。
        callback = parse.urlencode({'redirect_uri': 'http://127.0.0.1:8000/user/signup'})
        # 对回调地址进行编码，用户同意授权后将调用此链接。
        login_url = 'https://graph.qq.com/oauth2.0/token?grant_type=authorization_code&code=%s&client_id=%s&client_secret=%s&%s' % (
            code, client_id, client_secret, callback)  # 组织获取访问令牌的链接
        response = req.urlopen(login_url).read().decode()  # 打开获取访问令牌的链接
        access_token = re.split('&', response)[0]  # 获取访问令牌
        res = req.urlopen('https://graph.qq.com/oauth2.0/me?' + access_token).read().decode()  # 打开获取openid的链接
        openid = json.loads(parse_jsonp(res))['openid']  # 从返回数据中获取openid
        userinfo = req.urlopen('https://graph.qq.com/user/get_user_info?oauth_consumer_key=%s&openid=%s&%s' % (
            client_id, openid, access_token)).read().decode()  # 打开获取用户信息的链接
        userinfo = json.loads(userinfo)  # 将返回的用户信息数据（JSON格式）读取为字典。
        user = User.objects.filter(last_name=openid)  # 查询是否已存在用户
        if not user:  # 如果不存在用户
            user = User()  # 创建新用户
            user.last_name = openid  # 写入用户信息
            user.first_name = userinfo['nickname']  # 写入用户信息
            user.email = userinfo['figureurl_qq_1']  # 写入用户信息
            user.save()  # 保存或更新用户
        else:
            user = User.objects.get(last_name=openid)
        request.session['openid'] = openid  # 将已登录的用户openid写入Session
        if not user.username:
            return redirect(reverse('USER:bing',kwargs={'user_head':user.email}))
        else:
            login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('授权失败！')


def bing(request,user_head):
    if request.method == 'GET':
        return render(request,'bing.html',{'user_head':user_head})
    else:
        openid = request.session['openid']
        user = User.objects.get(last_name=openid)
        username = request.POST.get('user_id')
        if User.objects.filter(username=username):
            return render(request,'bing.html',{'user_head':user_head,'errmsg':'该用户已经注册过了！'})
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return render(request,'bing.html',{'user_head':user_head,'errmsg':'两次密码不一致'})
        else:
            user.first_name = user.first_name
            user.username = request.POST.get('username')
            user.set_password(password1)
            user.save()
            login(request,user)
            return redirect(reverse('ITEM:index'))

def parse_jsonp(jsonp_str):
    try:
        return re.search('^[^(]*?\((.*)\)[^)]*$', jsonp_str).group(1)
    except:
        raise ValueError('无效数据！')

def send_email(user_id, html_message ):
    subject = '失物招领-激活邮件'


    sender = '13986717767@163.com'

    pwd = 'Tuzhipeng00'
    receivers = user_id

    message = MIMEText(html_message, 'html', 'utf-8')  # 发送含HTML内容的邮件
    message['To'] = receivers
    message['From'] = sender

    message['Subject'] = Header(subject, 'utf-8')  # 也可以设置编码

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.163.com', 465)
        smtpObj.login(sender, pwd)  # 登录认证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送邮件主题
        print('邮件发送成功！')
    except smtplib.SMTPException as e:
        print('邮件发送失败，失败原因：', e)

class register_view(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST.get('user_name')
        username = request.POST.get('user_id')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if not all([first_name, password1,password2, username]):
            # 数据不完整
            return render(request, 'register.html',
                          {'errmsg': '数据不完整', 'first_name': first_name, 'username': username,
                           'password1': password1, 'password2': password2})
        if password2 != password1:
            return render(request, 'register.html',
                          {'errmsg': '两次密码不一样', 'first_name': first_name, 'username': username,
                           'password1': password1, 'password2': password2})
        elif len(password1) < 6:
            return render(request, 'register.html',
                          {'errmsg': '密码至少6位数', 'first_name': first_name, 'username': username,
                           'password1': password1, 'password2': password2})

            # 发邮件

        if re.match(r'^[1][3,4, 5,7,8,9][0-9]{9}$', username):
            if User.objects.filter(username=username):
                return render(request, 'register.html',
                              {'errmsg': '该用户已被注册', 'first_name': first_name, 'username': username,
                               'password1': password1, 'password2': password2})

            user = User.objects.create_user(username=username, first_name=first_name, password=password1,is_active=1)
            login(request, user)
            return redirect(reverse('ITEM:index'))

        elif re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', username):
            user = User.objects.filter(username=username)
            if user:
                user = User.objects.get(username=username)
                if user.is_active == 0:
                    user.delete()
                else:
                    return render(request, 'register.html', {'errmsg': '该用户已被注册','first_name':first_name,'username':username,'password1':password1, 'password2': password2})

            user = User.objects.create_user(username=username, first_name=first_name, password=password1, is_active=0)
            serializer = Serializer(settings.SECRET_KEY, 3600)
            info = {'confirm': user.id}
            token = serializer.dumps(info)  # bytes
            token = token.decode()
            html_message = '<h1>亲爱的%s, 欢迎注册失物招领网</h1>请点击下面链接激活您的账户<a href = "http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a><p>该链接一小时内有效</p>' % (
                user.first_name, token, token)
            send_email(user.username, html_message)
            return redirect(reverse('ITEM:index'))

        else:
            return render(request, 'register.html', {'errmsg': '手机格式或邮箱格式不正确','first_name':first_name,'username':username,'password1':password1, 'password2': password2})

        #return redirect(reverse('USER:login'), {'user_id_register':username})
class forget_view(View):
    def get(self, request):
        return render(request, 'forget.html')

    def post(self, request):
        username = request.POST.get('user_id')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not all([password1,password2, username]):
            # 数据不完整
            return render(request, 'forget.html',
                          {'errmsg': '数据不完整',  'username': username,
                           'password1': password1, 'password2': password2})
        if password2 != password1:
            return render(request, 'forget.html',
                          {'errmsg': '两次密码不一样',  'username': username,
                           'password1': password1, 'password2': password2})
        elif len(password1) < 6:
            return render(request, 'forget.html',
                          {'errmsg': '密码至少6位数',  'username': username,
                           'password1': password1, 'password2': password2})

            # 发邮件

        if re.match(r'^[1][3,4, 5,7,8,9][0-9]{9}$', username):
            try:
                user = User.objects.get(username=username)
            except:
                return render(request, 'forget.html',
                              {'errmsg': '该用户不存在',  'username': username,
                               'password1': password1, 'password2': password2})
            user.set_password(password1)
            login(request, user)
            return redirect(reverse('ITEM:index'))

        elif re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', username):
            try:
                user = User.objects.get(username=username)
            except:
                return render(request, 'forget.html',
                              {'errmsg': '该用户不存在',  'username': username,
                               'password1': password1, 'password2': password2})
            serializer = Serializer(settings.SECRET_KEY, 3600)
            info = {'confirm': user.id, 'password': password1}
            token = serializer.dumps(info)  # bytes
            token = token.decode()
            html_message = '<h1>亲爱的%s, 欢迎来到失物招领网</h1>请点击下面链接修改成您的新密码<a href = "http://127.0.0.1:8000/user/forget_password/%s">http://127.0.0.1:8000/user/active/%s</a><p>该链接一小时内有效</p>' % (
                user.first_name, token, token)
            send_email(user.username, html_message)
            return redirect(reverse('ITEM:index'))

        else:
            return render(request, 'forget.html', {'errmsg': '手机格式或邮箱格式不正确', 'username': username,
                               'password1': password1, 'password2': password2})

class active_view(View):
    def get(self, request, token):
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            user_id = info['confirm']
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            login(request,user)

            return redirect(reverse('ITEM:index'))
        except SignatureExpired:
            return redirect(reverse('USER:register'), {'errmsg':'激活链接已过期，请重新填写'})

class forget_change_view(View):
    def get(self, request, token):
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            user_id = info['confirm']
            password = info['password']
            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.save()
            login(request,user)

            return redirect(reverse('ITEM:index'))
        except SignatureExpired:
            return redirect(reverse('USER:register'), {'errmsg':'激活链接已过期，请重新填写'})
class login_view(View):
    def get(self, request):
        if 'user_id' in request.COOKIES:
            user_id = request.COOKIES.get('user_id')
            password = request.COOKIES.get('password')
            checked = 'checked'
        else:
            user_id = ''
            password = ''
            checked = ''
        return render(request, 'login.html', {'user_id':user_id,'password':password,'checked':checked})


    def post(self, request):
        username = request.POST.get('user_id')
        password = request.POST.get('password')
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg':'数据不完整'})
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            next_url = request.GET.get('next', reverse('ITEM:index'))
            print(next_url)
            response =  redirect(next_url)
            remember = request.POST.get('remember')
            if remember == 'on':
                response.set_cookie('user_id',username, max_age=7*24*3600)
                response.set_cookie('password', password, max_age=7*24*3600)
            else:
                response.delete_cookie('user_id')
            return response
        else:
            return render(request, 'login.html', {'errmsg':'用户名或密码错误', 'user_id': username, 'password':password})

class logout_view(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return redirect(reverse('ITEM:index'))

class my_release_view(LoginRequiredMixin, View):
    def get(self, request, user_password):
        try:
            user = User.objects.get(password=user_password)
            print(user)
            item = user.item_set.all()
            # item = Item.objects.get(item_user_id=user.id)

        except User.DoesNotExist:
            return redirect(reverse('ITEM:index'))
        return render(request, 'myRelease.html', {'items':item})

    def post(self, request):
        return render(request, 'login.html')

class my_change(LoginRequiredMixin, View):
    def get(self, request, user_password):
        print(user_password)

        return render(request, 'revision.html' )

    def post(self, request, user_password):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'revision.html', {'errmsg': '用户密码错误', 'username':username, 'password':password, 'password1':password1, 'password2':password2})

        elif password1 != password2:
            return render(request, 'revision.html', {'errmsg': '两次密码不一致','username':username, 'password':password, 'password1':password1, 'password2':password2})
        elif len(password1) < 6:
            return render(request, 'revision.html',
                          {'errmsg': '密码至少6位数', 'username': username, 'password': password, 'password1': password1,
                           'password2': password2})
        else:
            user.set_password(password1)
            user.first_name = first_name
            user.save()
            login(request, user)

        return redirect(reverse('USER:my_release', kwargs={'user_password':user_password}))


class my_contact(LoginRequiredMixin, View):
    def get(self, request, user_password):
        user = User.objects.get(password=user_password)
        return render(request, 'contact.html')

    def post(self, request, user_password):
        content = request.POST.get('content')
        suggestion = Suggestion(content=content)
        user = User.objects.get(password=user_password)
        suggestion.username = user.username
        suggestion.user_id = user
        suggestion.save()
        return redirect(reverse('USER:my_release', kwargs={'user_password':user_password}))

def my_delete(request,item_id, user_password):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect(reverse('USER:my_release', kwargs={'user_password': user_password}))

def my_found(request, item_id, user_password):
    item = Item.objects.get(id=item_id)
    item.is_found = True
    item.save()
    return redirect(reverse('USER:my_release', kwargs={'user_password': user_password}))


