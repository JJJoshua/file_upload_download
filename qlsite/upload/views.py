# -*- coding: UTF-8 -*-
import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
# --------default argus used for connect to OpenStack Cloud----
auth_username = 'admin'
auth_password = 'os62511279'
auth_url = 'http://202.112.113.220:5000/v2.0/'
project_name = 'admin'
region_name = 'RegionOne'

system_admin_email = 'machenyi2011@163.com'


#上传文件


#验证输入的镜像名是否可用
def valid_name(name):
    from repo_manage.models import VMImage
    if VMImage.objects.filter(name=name):
        return False
    return True


#上传镜像到服务器本地
def upload_image_file(image_file):
    pass



def upload_image_to_openstack(request):

    #当前用户信息
    user_id = 1

    from forms import upload_form
    if request.method == "POST":  # 请求方法为POST时，进行处理
        # 取出表格中内容
        rf = upload_form(request.POST)
        image_name = rf.data['file_name']

        #验证名字是否可用
        if ~valid_name(image_name):
            return HttpResponse('the name is invalid!')

        #上传镜像到服务器本地
        image_file = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not image_file:
            return HttpResponse("no files for upload!")
        image_data = upload_image_file(image_file)


        #将镜像upload到OpenStack
        from api_test.image_resource_operation import upload_image
        from api_test.createconn import create_connection
        conn = create_connection(auth_url, region_name, project_name, auth_username, auth_password)
        upload_image(conn, image_name, image_data)

        #将文件信息写入数据库
        from repo_manage.models import VMImage
        new_image = VMImage()
        new_image.name = image_name
        new_image.owner_id = user_id
        new_image.is_shared = 'False'
        #其余Image信息补充

        new_image.save()

        return HttpResponse('Upload image!')

    else:
        rf = upload_form()
    return render(request, 'upload.html', {'rf':rf})






#上传文件的组件
def upload_file(request):
    from forms import upload_form
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        save_path = "/home/qinli/tmp" #文件存储的绝对路径
        destination = open(os.path.join(save_path, myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

        # 取出表格中内容
        rf = upload_form(request.POST)
        file_name = rf.data['file_name']
        file_desc = rf.data['file_desc']

        #将表格中内容存入数据库
        from models import file
        f = file(name=file_name)
        f.desc = file_desc
        file_path = save_path+'/'+myFile.name
        f.path = file_path
        f.save()


        response = "congrats. your file \""+ myFile.name + "\" has been uploaded."
        return HttpResponse(response)
    else:
        rf = upload_form()
    return render(request, 'upload.html', {'rf':rf})



#下载文件
from django.http import StreamingHttpResponse

def download_file(request):
    # do something...

    #使用迭代器加载文件，实现大文件的下载
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "/home/qinli/tmp/system_design.docx"

    #使用StreamingHttpResponse配合迭代器返回文件到页面
    response = StreamingHttpResponse(file_iterator(the_file_name))

    #设置内容的格式使之能下载到硬盘而非显示在页面
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response

