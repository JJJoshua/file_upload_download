"""qlsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import *
from upload.views import *
from repo_manage.views import *
from search.views import *
from share.views import *
from delete.views import *
from api_test.views import *
from update.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

#the way to call def
    url(r'^blog/$', home, name='home'),

    url(r'^upload_file/$', upload_file, name='upload_file'),
    url(r'^download_file/$', download_file, name='download_file'),

    url(r'^show_person/$', show_person, name='show_person'),
    url(r'^list_image/$', list_image, name='list_image'),
    url(r'^list_experiment/$', list_experiment, name='list_experiment'),
    url(r'^list_openstack_images/$', list_openstack_images, name='list_openstack_images'),

    url(r'^search/$', search, name='search'),

    url(r'^share_image/$', share_image, name='share_image'),
    url(r'^share_experiment/$', share_experiment, name='share_experiment'),

    url(r'^delete_experiment/$', delete_experiment, name='delete_experiment'),
    url(r'^delete_openstack_image/$', delete_openstack_image, name='delete_openstack_image'),

    url(r'^upload_test/$', upload_test, name='upload_test'),
    url(r'^upload_openstack_image/$', upload_openstack_image, name='upload_openstack_image'),

    url(r'^update_experiment/$', update_experiment, name='upload_openstack_image'),


]
