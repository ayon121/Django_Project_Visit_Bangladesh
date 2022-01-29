from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.conf import settings 
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model):
    title =  models.CharField(max_length=50)
    author = models.ForeignKey(User , on_delete= CASCADE)
    #body = models.TextField()
    body = RichTextField(blank = True , null = True)
    
    post_date = models.DateField(auto_now_add= True)
    likes = models.ManyToManyField(User,related_name= 'post_details')
    
    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)
    
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post , related_name='comments', on_delete= CASCADE)
    name = models.ForeignKey(User , on_delete= CASCADE)
    body = models.TextField()
    comment_date = models.DateField(auto_now_add= True)
    
    def __str__(self):
        return str(self.post.title) + ' | ' + str(self.name)
    



