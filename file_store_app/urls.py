# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 23:49
# @Author  : MLee
# @File    : urls.py
from . import views

try:
    from django.conf.urls import url
except ImportError:
    from django.urls import url

urlpatterns = [
    url('^upload/$', views.upload_file),
    url('^delete/(?P<file_name>.+)$', views.delete_file),
    url('^download/(?P<file_name>.+)$', views.download_file),
    url('^file-list/$', views.get_file_lists),
]
