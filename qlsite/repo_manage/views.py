# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.
#展示某用户的信息
def show_person(request):
    from models import User

    #当前用户信息
    #name = 'josh'
    user_id = 2

    dict = User.objects.filter(id=user_id)
    return render(request, 'show_person.html', {'user': dict})


#展示某用户拥有的所有镜像信息
def list_image(request):
    from models import User, VMImage

    #当前用户信息
    #name = 'david'
    user_id = 1

    #展示私有镜像信息
    #owner = User.objects.get(username=name)
    dict1 = VMImage.objects.filter(owner_id=user_id) #利用了外键的特性


    #展示公有镜像信息
    dict2 = VMImage.objects.filter(is_shared='True')
    dict = []
    dict.append(dict1)
    dict.append(dict2)
    return render(request, 'list_image.html', {'ilist':dict})

#展示某用户拥有的所有实验信息
def list_experiment(request):
    from models import Experiment

    #当前用户信息
    #name = 'josh'
    user_id = 2

    #展示私有实验信息
    dict1 = Experiment.objects.filter(exp_owner_id=user_id)


    #展示公有实验信息
    dict2 = Experiment.objects.filter(is_shared='True')
    dict = []
    dict.append(dict1)
    dict.append(dict2)
    return render(request, 'list_experiment.html', {'ilist':dict})


