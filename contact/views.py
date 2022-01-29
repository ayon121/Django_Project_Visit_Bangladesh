from django.shortcuts import render 
from .models import contact
from django.views.generic import  CreateView
from .forms import ContactForm
# Create your views here.
def contacts(request):
    conts = contact.objects.all()
    if request.method == 'POST':
            form =ContactForm(request.POST)
            if form.is_valid():
                form.save()
    else:
        form = ContactForm()
   
    return render(request,"contact.html",{'conts': conts ,'form' : form})



 