# -*- coding: UTF-8 -*-
import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
#上传文件
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

