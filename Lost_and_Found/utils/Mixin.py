#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhipeng time: 2018/11/26

from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin,cls).as_view(**initkwargs)
        return login_required((view))