from django.contrib import admin

# Register your models here.
from .models import Destination , Testimonials ,  NewPosts , NewsSidebar ,IntroItem , Footer

admin.site.register(Destination)
admin.site.register(Testimonials)
admin.site.register(NewPosts)
admin.site.register(NewsSidebar) 
admin.site.register(IntroItem) 
admin.site.register(Footer) 

