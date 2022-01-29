from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import  messages


class ContactForm (forms.ModelForm):
    class Meta:
        model =  messages
        fields = ('Name' ,'Email' , 'Body')
        