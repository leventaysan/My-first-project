from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import blog
from blog.forms import RegisterForm
from blog.forms import loginForm
from blog.models import post


def index(request):
    vals=post.objects.all()
    return  render (request,'index.html',locals())

def detay(request,url):
    val=post.objects.get(slug=url)
    val.okunmasayisi +=1
    val.save()
    return render(request,'detay.html',locals())

def register(request):
    form=RegisterForm()
    return render(request,'register.html',locals())

def login(request):
    form2=loginForm()
    return render(request,'login.html',locals())
