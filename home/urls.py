from unicodedata import name
from venv import create
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.signin,name='signin'),
    path('signin/',views.signin,name='signin'),
    path('loginuser/', views.loginuser, name ='loginuser'),
    # path('blogs/loginuser/', views.loginuser, name ='loginuser'),
    path('logoutuser/', views.logoutuser, name ='logoutuser'),
    path('blogs/',views.blogs,name='blogs'),
    path('Blogger/',views.Blogger,name='Blogger'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('search',views.search,name='search'),
    # path('register/',views.register, name ='register'),
    path("create/",views.create,name='create'),
    # path("create/add",views.addblog,name='addblog'),
    # /path("create/addblog",views.addblog,name='addblog'),
    
]
