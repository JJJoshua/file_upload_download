# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response

# Create your views here.

#公开或取消公开镜像
def share_image(request):
    from repo_manage.models import VMImage
    #当前用户名
    #username = 'david'
    user_id = 1

    #当前镜像信息
    image_id = 'test1'

    if VMImage.objects.filter(owner_id=user_id, image_id=image_id):
        image = VMImage.objects.get(owner_id=user_id, image_id=image_id)
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
    #username = 'josh'
    user_id = 2

    #当前实验信息
    #exp_name = 'NFS'
    exp_id = 1

    if Experiment.objects.filter(exp_owner_id=user_id, id=exp_id):
        experiment = Experiment.objects.get(exp_owner_id=user_id, id=exp_id)
        if experiment.is_shared == 'True':
            experiment.is_shared = 'False'
            experiment.save()
            return HttpResponse('experiment ' + str(exp_id) + ' is now private')
        if experiment.is_shared == 'False':
            experiment.is_shared = 'True'
            experiment.save()
            return HttpResponse('experiment ' + str(exp_id) + ' is now shared')

    else:
        return HttpResponse('input error')