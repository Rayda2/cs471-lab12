from django import forms
from .models import Book7
from .models import Student11
from .models import Student22
from .models import Product11

class Book7Form(forms.ModelForm):
    class Meta:
        model = Book7
        fields = ['title', 'author', 'price', 'edition']



class Student11Form(forms.ModelForm):

    class Meta:
        model = Student11
        fields = '__all__'



class Student22Form(forms.ModelForm):

    class Meta:
        model = Student22
        fields = '__all__'



class Product11Form(forms.ModelForm):

    class Meta:
        model = Product11
        fields = '__all__'