# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid 
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Task(models.Model):
    task_names = models.CharField(max_length=100)
    published_date = models.DateField()
    
    def __str__(self):
        return self.task_names

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    state_provivance = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField()
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True)
    
    
    
    def __str__(self):
        return self.first_name+" "+self.last_name

class Book(models.Model):
    title = models.TextField()
    publisher = models.ForeignKey(Publisher)
    author = models.ManyToManyField(Author)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    def __str__(self):
        return self.title
class User(AbstractUser):
    role= models.CharField(max_length=10, default='Admin')