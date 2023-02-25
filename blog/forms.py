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
        widget = {
            'film_title': form.TextInput(attrs={'class': 'form-control'}),
            'blogger': form.Select(attrs={'class': 'form-control'}),
            'slug': form.TextInput(attrs={'class': 'form-control'}),
            'director': form.TextInput(attrs={'class': 'form-control'}),
            'actor': form.TextInput(attrs={'class': 'form-control'}),
            'content': form.TextArea(attrs={'class': 'form-control'}),
        }
