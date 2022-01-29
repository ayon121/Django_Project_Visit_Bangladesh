from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Post ,Comment


class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' ,'body' , 'author')
        
        widgets = {
            'title' : forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'Type Your Post Title'}),
            'body' : forms.Textarea(attrs = {'class' : 'form-control' , 'placeholder' : 'Type Your Post'}),
            #'author' : forms.Select(attrs = {'class' : 'form-control'}),
            'author' : forms.TextInput(attrs = {'class' : 'form-control' ,'value' : '', 'id' : 'author' , 'type' : 'hidden'}),
        
   
        }
        
        
class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        
        widgets = {
            'name' : forms.TextInput(attrs = {'class' : 'form-control' ,'value' : '', 'id' : 'name' , 'type' : 'hidden'}),
        
            'body' : forms.Textarea(attrs = {'class' : 'form-control' , 'placeholder' : 'Type Your Commment'}),
   
        }
        
        

