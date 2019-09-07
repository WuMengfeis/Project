#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhipeng time: 2018/11/28
from haystack import indexes
from .models import Item
#指定对于某个类的某些数据建立索引
class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Item

    def index_queryset(self, using=None):
        return self.get_model().objects.all()