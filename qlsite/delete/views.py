# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def delete_experiment(request):
    from repo_manage.models import Experiment

    #当前用户信息，david的id是1
    user_id = 1

    #当前选择的实验，test exp的id是6
    exp_id = 7

    if Experiment.objects.get(id=exp_id).exp_owner_id == user_id:
        Experiment.objects.get(id=exp_id).delete()
        return HttpResponse('The experiment ' + str(exp_id) + ' has been deleted')
    else:
        return HttpResponse('delete error')
