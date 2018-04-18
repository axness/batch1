# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task
def python(request):
    return HttpResponse("python")
# Create your views here.
def index(request):
    #import pdb; pdb.set_trace()
    db_obj = Task.objects.all()
    return render(request, "index.html", {"obj": db_obj})

def first(request):
    return HttpResponse("this is a second page")

def detail(request, **kwargs):
    db_obj = Task.objects.get(id=kwargs['task_id'])
    return render(request, "detail.html", {'obj': db_obj})