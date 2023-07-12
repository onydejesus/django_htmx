from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title', 'author', 'number_of_pages'
        )
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "number_of_pages": forms.TextInput(attrs={'class': 'form-control'}),
            "author": forms.Select(attrs={'class': 'form-control'})

        }