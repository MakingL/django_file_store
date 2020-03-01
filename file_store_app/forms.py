# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 23:48
# @Author  : MLee
# @File    : forms.py
from django.forms import ModelForm

from .models import UploadedFile


class UploadFileForm(ModelForm):
    class Meta:
        model = UploadedFile
        fields = ["uploaded_file", ]
