# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#teacher info
class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    # role = models.CharField(max_length = 50,default = 'student')#teacher or student
    email = models.EmailField(blank=True)


    def __unicode__(self):
        return self.username


    class Meta:
        ordering = ['username']


#student info
class Student(models.Model):
    stu_username = models.CharField(max_length = 50)
    stu_password = models.CharField(max_length = 50)
    stu_email =  models.EmailField(blank=True)


    def __unicode__(self):
        return self.stu_username


    #set the specific order
    class Meta:
        ordering = ['stu_username']

#The db stores all VMimages in repo,both public repo and private repo(data from openstack)
class VMImage(models.Model):
    image_id = models.CharField(max_length = 36,null=True,blank=True)
    name = models.CharField(max_length = 255)
    owner = models.ForeignKey(User)
    own_project = models.CharField(max_length= 32,null=True)

    #暂时取消is_pulic，使用id+is_shared来管理权限
    #is_public = models.CharField(max_length = 10,default = 'YES')

    description = models.TextField(blank=True)
    status = models.CharField(max_length = 30,default = 'active')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True,null=True,blank = True)
    size = models.BigIntegerField()
    min_disk = models.IntegerField(default = 0)
    min_ram = models.IntegerField(default = 0)

    #暂时不用tag
    #tags = models.ManyToManyField('Tag')

    is_shared = models.CharField(max_length=10, null=True, default='False')
    shared_time = models.DateTimeField(auto_now_add=True, null=True,editable=True)
    flavor = models.CharField(max_length= 10,null = True,blank = True,default='m1.tiny')
    keypair = models.CharField(max_length= 20,null = True,blank = True,default='mykey')

    def __unicode__(self):
        return u'name=%s,creater=%s,is_shared=%s' % (self.name,self.owner,self.is_shared)

    class Meta:
        ordering = ['-created_at']

