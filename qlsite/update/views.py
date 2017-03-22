# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from repo_manage.models import VMImage,Experiment
from forms import update_exp_form
import datetime

# Create your views here.
def update_experiment(request):

    #用户信息,josh_id=2
    user_id = 2

    #实验信息
    exp_id = 1

    experiment = Experiment.objects.get(id=exp_id)
    image_list = experiment.exp_images.all()
    # 暂时不考虑网络资源，之后注释同样理由
    # networkList = experiment.exp_network.all()
    images_id_list = []
    # networks_idList = []
    for item in image_list:
        images_id_list.append(item.id)
    # for item in networkList:
    #     networks_idList.append(item.id)

    # edit and update the exp
    if request.method == 'POST':
        rf = update_exp_form(request.POST)
        # get input data from form
        update_name = rf.data['name']
        update_desc = rf.data['desc']
        #update_images_id_list = rf.data['images_id_list']
        update_images_id_list = request.POST.getlist('images_id_list')
        # update_networks_idList = rf.data['networks_id_list']
        update_guide = rf.data['guide']
        update_refer_result = rf.data['refer_result']

        update_image_list = []
        # update_networkList = []
        print "123"
        print update_images_id_list
        for i in update_images_id_list:
            update_image_list.append(VMImage.objects.get(id=i))
        # for i in update_networks_idList:
        #     update_networkList.append(Network.objects.get(id=i))

        # update basic info for exp
        re = Experiment.objects.filter(id=exp_id).update(exp_name=update_name, exp_description=update_desc,
                                                         exp_image_count=len(update_image_list), exp_guide=update_guide,
                                                         exp_result=update_refer_result,
                                                         exp_updatetime=datetime.datetime.now())
        update_e = Experiment.objects.get(id=exp_id)
        # update image list and network list for exp
        for i in range(0, len(update_image_list)):
            if update_image_list[i] not in image_list:
                update_e.exp_images.add(update_image_list[i])
                print "######"
                print update_image_list[i]
        for j in range(0, len(image_list)):
            if image_list[j] not in update_image_list:
                update_e.exp_images.remove(image_list[j])
                print "@@@@@"
                print update_image_list[i]

        # for item in update_networkList:
        #     if item not in networkList:
        #         update_e.exp_network.add(item)
        # for item in networkList:
        #     if item not in update_networkList:
        #         update_e.exp_network.remove(item)
        # refersh the exp list
        return HttpResponseRedirect('/update_experiment/')
    else:
        # initial the form
        attrs = {}
        attrs['name'] = experiment.exp_name
        attrs['desc'] = experiment.exp_description
        attrs['images_id_list'] = images_id_list
        # attrs['networks_idList'] = networks_idList
        attrs['guide'] = experiment.exp_guide
        attrs['refer_result'] = experiment.exp_result
        gf = update_exp_form(initial=attrs)
    return render_to_response("exp_update.html", {'rf': gf})


def update_image(request):
    pass