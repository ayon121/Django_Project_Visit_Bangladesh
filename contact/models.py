from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
class contact(models.Model):
    heading =  models.CharField(max_length=50)
    title =  models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.title)
    
    
class messages(models.Model):
    Name = models.CharField(max_length=50)
    Email =  models.CharField(max_length=50)
    Body =  models.TextField()
    
    
    def __str__(self):
        return str(self.Name)  + ' | ' +  str(self.Email)
    