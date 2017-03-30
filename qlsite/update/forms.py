# -*- coding: UTF-8 -*-
from django import forms
from repo_manage.models import VMImage, Experiment

class update_exp_form(forms.Form):
    name = forms.CharField(label='Exp Name', max_length=150)
    desc = forms.CharField(label='Description', max_length=500,
                           widget=forms.Textarea(),
                           required=False)
    images_id_list = forms.MultipleChoiceField(label='Include Images',
                                              widget=forms.CheckboxSelectMultiple,
                                              )
    guide = forms.CharField(label="Guide",
                            widget=forms.Textarea(),
                            required=False)
    refer_result = forms.CharField(label="Refer Result",
                                   widget=forms.Textarea(),
                                   required=False, )

    def __init__(self,*args,**kwargs):
        super(update_exp_form, self).__init__(*args, **kwargs)
        self.fields['images_id_list'].choices = [(i.pk, i.name) for i in VMImage.objects.all()]

class update_exp_form1(forms.ModelForm):
    name = forms.CharField(label='Exp Name', max_length=150)
    desc = forms.CharField(label='Description', max_length=500,
                           widget=forms.Textarea(),
                           required=False)
    # images_id_list = forms.MultipleChoiceField(label='Include Images',
    #                                           widget=forms.CheckboxSelectMultiple,
    #                                           )
    guide = forms.CharField(label="Guide",
                            widget=forms.Textarea(),
                            required=False)
    refer_result = forms.CharField(label="Refer Result",
                                   widget=forms.Textarea(),
                                   required=False, )

    # def __init__(self,*args,**kwargs):
    #     super(update_exp_form, self).__init__(*args, **kwargs)
    #     self.fields['images_id_list'].choices = [(i.pk, i.name) for i in VMImage.objects.all()]


    class Meta:
        model = Experiment
        fields = ['exp_images']


