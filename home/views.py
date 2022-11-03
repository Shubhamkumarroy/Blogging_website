from audioop import reverse
from cmath import log
import email
from fnmatch import fnmatch
from re import template
import re
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from home.models import Blog
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def home(request):
    return render(request, "home.html")

def blogs(request):
    return render(request,'leter.html')
def signin(request):
    template=loader.get_template('sign.html')
    return HttpResponse(template.render({},request))

# def fn():
#     return redirect("/")

def loginuser(request):
    if request.method=="post":
       return redirect("/")
        
    return render(request,'home.html')

def create(request):
    if request.method == "POST":
        title = request.POST.get('title','')
        description = request.POST.get('description', '')
        obj = Blog(title=title, description=description)
        obj.save()
        return redirect('/blogs/')
    else:
        return render(request,'create.html')

def logoutuser(request):
    logout(request)
    return redirect("/")

def blogs(request):
    mydata=Blog.objects.all()
    t=loader.get_template('print.html')
    context={'y':mydata}
    return HttpResponse(t.render(context,request))

def Blogger(request):
    return render(request,'home.html')
def delete(request,id):
    obj_list = Blog.objects.filter(id=id)
    print(obj_list)
    if len(obj_list) != 0:
        obj = obj_list[0]
        print(obj)
        obj.delete()
    return redirect('/blogs/')

def edit(request,id):
    obj=Blog.objects.filter(id=id)
    o1=obj[0]
    print(o1)
    tem=loader.get_template('edit.html')
    context={'ed':o1}
    return HttpResponse(tem.render(context, request))
    # return render(request,'home.html')
def update(request,id):
    title = request.POST['title']
    description= request.POST['description']
    member = Blog.objects.get(id=id)
    member.title = title
    member.description =description
    member.save()
    return redirect('/blogs/')



