from django import forms
from .models import Book

class ExampleForm(forms.Form):  # MUST HAVE THIS EXACT CLASS NAME
    """Example form for security demonstration"""
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class BookForm(forms.ModelForm):
    """Form for book creation and editing with validation"""
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
