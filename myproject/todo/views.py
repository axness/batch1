# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
def python(request):
    return HttpResponse("python")
# Create your views here.
def index(request):
    return HttpResponse("this is a index page")

def first(request):
    return HttpResponse("this is a second page")
