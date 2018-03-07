# coding=utf-8
from __future__ import unicode_literals
import sys
print sys.getdefaultencoding()

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    '''
    Bu model kulllanıcı sınıfımız olacaktır.
    '''
    adres=models.CharField(max_length=250)
    tel=models.CharField(max_length=250)
    bio=models.TextField()
    github=models.URLField()
    linkedin=models.URLField()
    resim=models.ImageField(upload_to='kullanici_resimleri', default='resim.png')