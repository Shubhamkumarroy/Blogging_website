import email
from operator import mod
from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.pk)
