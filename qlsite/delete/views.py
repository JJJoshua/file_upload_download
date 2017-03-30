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


def delete_openstack_image(request):
    from repo_manage.models import VMImage
    from api_test import createconn, image_resource_operation

    # --------default argus used for connect to OpenStack Cloud----
    auth_username = 'admin'
    auth_password = 'os62511279'
    auth_url = 'http://202.112.113.220:5000/v2.0/'
    project_name = 'admin'
    region_name = 'RegionOne'

    system_admin_email = 'machenyi2011@163.com'

    #当前用户信息，josh的id是2
    user_id = 2

    #当前选择的镜像，name为qinli_cirros_test
    image_name = 'qinlitest'

    img = VMImage.objects.get(name=image_name)

    if img.owner_id == user_id:
        image_id = img.image_id #image_id存的是openstack中的image_id
        conn = createconn.create_connection(auth_url, region_name, project_name, auth_username, auth_password)

        #删除OpenStack中的镜像
        image_resource_operation.delete_image(conn, image_id)

        #删除数据库中记录
        img.delete()

        return HttpResponse('the image ' + image_name+ ' has been deleted')
    else:
        return HttpResponse('you can\'t delete the image')