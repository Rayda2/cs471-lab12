from django import forms
from .models import Book7

class Book7Form(forms.ModelForm):
    class Meta:
        model = Book7
        fields = ['title', 'author', 'price', 'edition']