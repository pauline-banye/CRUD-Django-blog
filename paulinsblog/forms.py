from django import forms
from .models import Post, Comment
from django.forms.widgets import NumberInput
from django.utils import timezone # for the date/time

# created custom form
class BlogForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_image', 'author', 'post', 'date_published')
        #fields = ('title', 'author', 'intro', 'post', 'date_published')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.Select(attrs={'class':'form-control'}),
            #'intro' : forms.TextInput(attrs={'class':'form-control'}),
            'post' : forms.Textarea(attrs={'class':'form-control'}),
            'date_published': NumberInput(attrs={'type':'datetime'}),
        }

class CommentForm(forms.ModelForm): # created a form for our comments section
    class Meta:
        model = Comment
        fields = ('writer', 'review')
       
        widgets = {
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'post' : forms.Textarea(attrs={'class':'form-control'}),
        }

