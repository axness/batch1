# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task, Book, Author
from django.views.generic import ListView, DetailView, CreateView
from todo.forms import AuthorForm, BookForm
from django.http.response import HttpResponseRedirect
from django.views.generic import View
from oauthlib.uri_validate import query
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def python(request):
    return HttpResponse("python")
# Create your views here.
@login_required
def index(request):
    print request.user.is_authenticated
    db_obj = Task.objects.all()
    return render(request, "index.html", {"obj": db_obj})

#def login(request):
#    form = AuthenticationForm(request)
#    import pdb; pdb.set_trace()
#    if form.is_valid():
#        #import pdb; pdb.set_trace()
#        pass
#    return render(request, 'login.html', {'form': AuthenticationForm()})

def first(request):
    return HttpResponse("this is a second page")

def detail(request, **kwargs):
    db_obj = Task.objects.get(id=kwargs['task_id'])
    return render(request, "detail.html", {'obj': db_obj})
@login_required()
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

class BookList(ListView):
    model = Book
    template_name = 'books.html' 

class AddAuthor(CreateView):
    #import pdb; pdb.set_trace()
    
    form = AuthorForm()
    model = Author
    fields = '__all__'
    template_name = 'add_author.html'
    success_url = '/thanks/'
    
    def post(self, request):
        form = AuthorForm(request.POST)
        obj = Author()
        print(form)
        data = form.cleaned_data
        obj.email = data['email']
        obj.first_name = data['first_name']
        obj.last_name = data['last_name']
        obj.save()
        return HttpResponse("success")
    
class AuthorDetail(LoginRequiredMixin, DetailView):
    model = Author
    template_name = 'author_detail.html'