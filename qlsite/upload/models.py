# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class file(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    path = models.CharField(max_length=300)

