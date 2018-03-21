from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import blog
from blog.models import post


def index(request):
    vals=post.objects.all()
    return  render (request,'index.html',locals())

def detay(request,url):
    val=post.objects.get(slug=url)
    return render(request,'detay.html',locals())