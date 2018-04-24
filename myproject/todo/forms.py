from django import forms
from todo.models import Book, Author, Publisher

class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    
class BookForm(forms.Form):
    title = forms.CharField(max_length=50)
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.values_list('name', flat=True).distinct())
    
    #class Meta:
    #    model = Book
    #    fields = ['name', 'publisher']
        