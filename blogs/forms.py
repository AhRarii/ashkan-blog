from django import forms
from .models import BlogPost


class BlogFrom(forms.ModelForm):
    """A form for creating blog posts."""
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': ''}
