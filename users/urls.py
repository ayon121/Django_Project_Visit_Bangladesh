from django.urls import path 
from . import views
urlpatterns = [
    path('Register' ,views.register , name= 'register'),
    path('Login' ,views.loginuser , name = 'login'),
    path('Logout' ,views.logoutuser , name= 'logout'),
]
