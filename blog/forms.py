from .models import Comment, Post
from django import forms

#class to create a model to hanbdle form processing and validation
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# form fields for ous post model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('film_title','blogger', 'slug', 'director', 'actor', 'content')
        # creates a dictonary for the form using bootstrap form control
        widgets = {
            'film_title': forms.TextInput(attrs={'class': 'form-control'}),
            'blogger': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'actor': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextArea(attrs={'class': 'form-control'})
        }
