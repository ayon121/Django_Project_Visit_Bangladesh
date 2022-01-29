from django.urls import path 
from . import views
from .views import search_Destination
urlpatterns = [
    path('' ,views.home , name= 'home'),
    path('search' ,views.search_Destination , name= 'search'),
    
]

