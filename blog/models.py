from __future__ import unicode_literals


from django.db import models

# Create your models here.
from proje.settings import AUTH_USER_MODEL


class post(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    author=models.ForeignKey(AUTH_USER_MODEL)
    content=models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="resimler",default="resimler/resim.png")

