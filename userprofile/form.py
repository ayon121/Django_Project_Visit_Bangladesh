from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs ={'class' : 'form-control' , 'type' : 'password'} ))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs ={'class' : 'form-control' , 'type' : 'password'} ))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs ={'class' : 'form-control' , 'type' : 'password'} ))
    
    class Meta:
        model = User
        fields = ['old_password' ,'new_password1', 'new_password2' ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email' ]
    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image' ,'Fullname', 'Bio' ,'Phone_number' ,  'State', 'City', 'Street' ,'Zip' ]
        
        

        