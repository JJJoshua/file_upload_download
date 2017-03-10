# -*- coding: UTF-8 -*-
from django import forms

class upload_form(forms.Form):
    myfile = forms.FileField(required=True)
    file_name = forms.CharField(max_length=50, required=True)
    file_desc = forms.CharField(max_length=200, required=False)
