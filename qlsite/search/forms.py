# -*- coding: UTF-8 -*-
from django import forms

class search_form(forms.Form):
    id = forms.CharField(max_length=50, required=False) #id是image特有的，实验没有
    name = forms.CharField(max_length=50, required=False)
    owner = forms.CharField(max_length=50, required=False)