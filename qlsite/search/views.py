# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def search(request):
    from repo_manage.models import VMImage, Experiment
    from forms import search_form
    if request.method == "POST":
        rf = search_form(request.POST)

        #当前用户名
        username = 'josh'

        if rf.is_valid():
            id = rf.cleaned_data['id']
            name = rf.cleaned_data['name']
            owner = rf.cleaned_data['owner']

        #处理Image部分
            #根据当前用户信息得到的其可见的Image
            private_ilist = list(VMImage.objects.filter(owner__username=username))
            shared_ilist = list(VMImage.objects.filter(is_shared='True'))
            #可见的Image为公有和私有的并集
            own_ilist = list(set(private_ilist) | set(shared_ilist))


            #id选项非空，则筛选出符合要求的Image，取交集
            if id:
                id_ilist = list(VMImage.objects.filter(image_id=id))
                own_ilist = list(set(own_ilist) & set(id_ilist))


            #name选项非空，则筛选出符合要求的Image，取交集
            if name:
                name_ilist = list(VMImage.objects.filter(name=name))
                own_ilist = list(set(own_ilist) & set(name_ilist))

            # owner选项非空，则筛选出符合要求的Image，取交集
            if owner:
                owner_ilist = list(VMImage.objects.filter(owner__username=owner))
                own_ilist = list(set(own_ilist) & set(owner_ilist))





        #处理Experiment部分
            # 根据当前用户信息得到的其可见的Experiment
            private_elist = list(Experiment.objects.filter(exp_owner__username=username))
            shared_elist = list(Experiment.objects.filter(is_shared='True'))
            # 可见的Image为公有和私有的并集
            own_elist = list(set(private_elist) | set(shared_elist))


            # name选项非空，则筛选出符合要求的Experiment，取交集
            if name:
                name_elist = list(Experiment.objects.filter(exp_name=name))
                own_elist = list(set(own_elist) & set(name_elist))

            # owner选项非空，则筛选出符合要求的Experiment，取交集
            if owner:
                owner_elist = list(Experiment.objects.filter(exp_owner__username=owner))
                own_elist = list(set(own_elist) & set(owner_elist))





            own_list = []
            own_list.append(own_ilist)
            own_list.append(own_elist)

            return render(request, 'search_result.html', {'list': own_list})

        else:
            return HttpResponse('invalid input')

    else:
        rf = search_form()
    return render(request, 'search.html', {'rf': rf})