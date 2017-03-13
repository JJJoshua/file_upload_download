# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response

# Create your views here.

#公开或取消公开镜像
def share_image(request):
    from repo_manage.models import VMImage
    #当前用户名
    username = 'david'

    #当前镜像信息
    image_id = 'test1'

    if VMImage.objects.filter(owner__username=username, image_id=image_id):
        image = VMImage.objects.get(owner__username=username, image_id=image_id)
        if image.is_shared == 'True':
            image.is_shared = 'False'
            image.save()
            return HttpResponse('image ' + image_id + ' is now private')
        if image.is_shared == 'False':
            image.is_shared = 'True'
            image.save()
            return HttpResponse('image ' + image_id + ' is now shared')

    else:
        return HttpResponse('input error')




def share_experiment(request):
    from repo_manage.models import Experiment
    #当前用户名
    username = 'josh'

    #当前实验信息
    exp_name = 'NFS'

    if Experiment.objects.filter(exp_owner__username=username, exp_name=exp_name):
        experiment = Experiment.objects.get(exp_owner__username=username, exp_name=exp_name)
        if experiment.is_shared == 'True':
            experiment.is_shared = 'False'
            experiment.save()
            return HttpResponse('experiment ' + exp_name + ' is now private')
        if experiment.is_shared == 'False':
            experiment.is_shared = 'True'
            experiment.save()
            return HttpResponse('experiment ' + exp_name + ' is now shared')

    else:
        return HttpResponse('input error')