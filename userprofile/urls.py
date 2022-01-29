from re import template
from django.urls import path
from . import views
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('YourProfile' ,views.userprofiles  , name= 'profile'),
    path('EditProfile' ,views.profile),
    #path ('Password' ,auth_views.PasswordChangeView.as_view(template_name= 'change_password.html' ))
    path ('Password' ,PasswordsChangeView.as_view(template_name= 'change_password.html' ))


 
    
]

