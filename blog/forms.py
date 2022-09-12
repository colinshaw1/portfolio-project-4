from .models import Comment
from django import forms

#class to create a model to hanbdle form processing and validation
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ('name', 'email')