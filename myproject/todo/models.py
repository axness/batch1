# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
    task_names = models.CharField(max_length=100)
    published_date = models.DateField()