# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from todo.models import Task, Book, Publisher, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher')
    search_fields = ('title', 'author')
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
admin.site.register(Task)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
