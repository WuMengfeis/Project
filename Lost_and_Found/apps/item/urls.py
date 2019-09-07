#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhipeng time: 2018/11/19
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('release/', views.release_view.as_view(), name='release'),
    path('search/', views.search, name='search'),
    path('index_search/',views.index_search,name='index_search'),
    url(r'^detail/(?P<item_id>\d+)$', views.detail_view.as_view(), name='detail'),
    url(r'item_edit/(?P<item_id>\d+)$', views.item_edit, name = 'item_edit'),
    path('lost/',views.lost,name='lost'),
    path('found/',views.found,name='found'),
    path('all_found/',views.all_found,name='all_found')
]