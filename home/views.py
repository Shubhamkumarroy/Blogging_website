from audioop import reverse
from cmath import log
import email
from fnmatch import fnmatch
from re import template
import re
from sqlite3 import Timestamp
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from home.models import Blog,Newuser,newBlog
from django.template import loader
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from django.forms import NameForm


# Create your views here.
def home(request):
    return render(request, "home.html")
def landing(request):
    return render(request,'loginpage.html')

def signup(request):
    if request.method=="POST":
        # print(-1)
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        return render(request,"home.html")

def loginuser(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            id1=user.id
            return redirect('/home/')
        else:
            return render(request,'loginpage.html',{'username':username})
        
def logoutuser(request):
    logout(request)
    return render(request,'loginpage.html')

def signin(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render({},request))
def register(request):
    return render(request,'signup.html')
def accountcreate(request):
    return render(request, 'home.html')

def create(request,id1):
    if request.method == "POST":
        title = request.POST.get('title','')
        description = request.POST.get('description', '')
        id1=id1
        user=request.user
        username=user.username
        obj1=newBlog(title=title,description=description,id1=id1,username=username)
        obj1.save()
        return redirect('/blogs/')
    else:
        
        # print(user.fname)
        return render(request,'create.html')

        # if len(user)!=0:
            

        


def blogs(request):
    mydata=newBlog.objects.all().order_by('-timestamp')
    t=loader.get_template('print.html')
    obj_list=list(mydata)
    context={'y':mydata}
    return HttpResponse(t.render(context,request))

def Blogger(request):
    return render(request,'home.html')

@login_required
def delete(request,id):
    query_list = newBlog.objects.filter(id=id)
    obj_list=list(query_list)
    x=obj_list[0]
    flag=False
   
    if x.username==request.user.username and query_list.count()!=0:
        obj=obj_list[0]
        obj.delete()
        flag=True
        return redirect('/blogs/')
    else:
        messages.error(request,"You can't delete this blog because u are not author of this")
        return redirect('/blogs/')
       
        




def edit(request,id):
    obj=newBlog.objects.filter(id=id)
    obj_list=list(obj)
    x=obj_list[0]
    o1=obj[0]
    tem=loader.get_template('edit.html')
    context={'ed':o1}
    if x.username==request.user.username and obj.count()!=0:
        obj=obj_list[0]
        obj.delete()
        flag=True
        return HttpResponse(tem.render(context, request))
    else:
        messages.error(request,"You can't edit this blog because u are not author of this")
        return redirect('/blogs/')
    
def update(request,id):
    title = request.POST['title']
    description= request.POST['description']
    member = newBlog.objects.get(id=id)
    member.title = title
    member.description =description
    member.save()
    return redirect('/blogs/')
def search(request):
    if request.method=='GET':
        id1=request.GET['search_blog']
        obj=newBlog.objects.all()
        t=loader.get_template('search_blog.html')
        context={'y':obj,'id1':id1}
        return HttpResponse(t.render(context,request))
    else:
        return render(request,'home.html')
        


