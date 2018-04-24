# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task
from django.views.generic import ListView, DetailView
from todo.forms import AuthorForm, BookForm
from django.http.response import HttpResponseRedirect


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

def add_book(request):
    #import pdb; pdb.set_trace()
    form = BookForm(request.GET)
    if form.is_valid():
        return HttpResponseRedirect('/thanks/')
    form = BookForm()
    return render(request, 'add_book.html', {'form1': form})

def add_author(request):
    #import pdb; pdb.set_trace()
    form =  AuthorForm(request.GET)
    if form.is_valid():
        #
        return HttpResponse('thanks for adding a author')
    form = AuthorForm()
    return render(request, 'add_author.html', {'form1': form})