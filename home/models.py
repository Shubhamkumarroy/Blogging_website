import email
from operator import mod
from sqlite3 import Timestamp
import uuid
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # uniqueid = models.UUIDField(default=uuid.uuid4, editable=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.pk)


class newBlog(models.Model):
      title = models.CharField(max_length=100)
      description=models.TextField()
      id1=models.IntegerField()
      username=models.CharField(max_length=20,default='shubham')
      timestamp = models.DateTimeField(auto_now_add=True)
      def __str__(self):
        return str(self.pk)
      
      
    	
      
    
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'password1', 'password2']
                

class Newuser(models.Model):
      username=models.CharField(max_length=20)
      fname=models.CharField(max_length=20)
      lname=models.CharField(max_length=20)
      email=models.EmailField()
      password=models.CharField(max_length=20)
      

