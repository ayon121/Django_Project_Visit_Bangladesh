from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Bio = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to= 'profile_pics')
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    Zip = models.IntegerField()
    Fullname = models.CharField(max_length=50)
    
    
    def __str__(self):
        return str(self.user.username)
    

  