from django.db import models
from django.utils import timezone
#Create your models here.

class IntroItem(models.Model):
    img = models.ImageField(upload_to = 'pics')
    title = models.CharField(max_length=50)
    subtitle= models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.title)




class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default= False)
    post_url = models.CharField(max_length=100)
   
    def __str__(self):
        return str(self.name)
    
class Testimonials(models.Model):
    img = models.ImageField(upload_to = 'pics')
    subtitle= models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    testimonial_author =  models.CharField(max_length=100)
    author_position = models.CharField(max_length=100)

    
    def __str__(self):
        return str(self.title)
    

class NewPosts(models.Model):
    img = models.ImageField(upload_to = 'pics')
    date =  models.IntegerField()
    month = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    subtitle= models.CharField(max_length=50)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.title)
    
    
class NewsSidebar(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.title)
    
    
class Footer(models.Model):
    img = models.ImageField(upload_to = 'pics')
    company_name = models.CharField(max_length=50)
    year =  models.IntegerField()