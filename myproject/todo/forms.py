from django import forms

class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    
    