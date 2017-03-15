# -*- coding: UTF-8 -*-
from django.shortcuts import render
from image_resource_operation import *
from createconn import *
from extract_openstack_data import *
from django.http import HttpResponse

# Create your views here.






def list_openstack_images(request):
    # --------default argus used for connect to OpenStack Cloud----
    auth_username = 'admin'
    auth_password = 'os62511279'
    auth_url = 'http://202.112.113.220:5000/v2.0/'
    project_name = 'admin'
    region_name = 'RegionOne'

    system_admin_email = 'machenyi2011@163.com'

    #创建连接
    conn = create_connection(auth_url, region_name, project_name, auth_username, auth_password)

    #list，返回值是一个字典列表
    list = list_images(conn)

    return HttpResponse('11')
