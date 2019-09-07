#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhipeng time: 2018/11/19
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('register', views.register_view.as_view(), name='register'),
    path('forget', views.forget_view.as_view(), name='forget'),
    url(r'^active/(?P<token>.*)$', views.active_view.as_view(), name='active'),
    url(r'^forget_password/(?P<token>.*)$', views.forget_change_view.as_view(), name='active'),
    path('login', views.login_view.as_view(), name='login'),
    path('logout', views.logout_view.as_view(), name='logout'),
    path('to_login/', views.to_login, name='to_login'),
    path('signup/', views.QQ_login, name='QQ_login'),
    url(r'^bing/(?P<user_head>.*)$', views.bing, name='bing'),
    url(r'^my_release/(?P<user_password>.*)$', views.my_release_view.as_view(), name='my_release'),
    url(r'^my_change/(?P<user_password>.*)$', views.my_change.as_view(), name='my_change'),
    url(r'^my_contact/(?P<user_password>.*)$', views.my_contact.as_view(), name='my_contact'),
    url(r'my_delete/(?P<item_id>\d+)/(?P<user_password>.*)$', views.my_delete, name ='my_delete'),
    url(r'my_found/(?P<item_id>\d+)/(?P<user_password>.*)$', views.my_found, name='my_found')
]