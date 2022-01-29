from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .form import UserUpdateForm ,ProfileUpdateForm ,PasswordChangingForm
from django.contrib import messages


from django.contrib.auth.views import PasswordChangeView ,PasswordChangeForm
from django.urls import reverse_lazy 
# Create your views here.
def userprofiles(request):
    if request.user.is_authenticated:
        current_user = request.user
        username = current_user.username
        useremail = current_user.email
        
        current_user_profile = request.user.profile
        userbio  = current_user_profile.Bio
        
        userfullname  = current_user_profile.Fullname
        userphone  = current_user_profile.Phone_number
        usercity  = current_user_profile.City
        usersate  = current_user_profile.State
        userstreet = current_user_profile.Street
        userzip  = current_user_profile.Zip
        
        
        return render(request , 'userprofile.html' , {'user_name' : username , 
                                                      'user_email' :useremail , 
                                                      'link' :  'http://127.0.0.1:8000/profile/EditProfile',
                                                      'link1' : 'http://127.0.0.1:8000/',
                                                      'link2': 'http://127.0.0.1:8000/profile/Password',
                                                      'user_bio' : userbio,
                                                      'user_fullname': userfullname,
                                                      'user_phone' : userphone,
                                                      'user_city' :usercity,
                                                      'user_sate' : usersate,
                                                      'user_street' : userstreet,
                                                      'user_zip': userzip})
    
    
    
    else:
        return redirect('register')
    
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm( request.POST ,instance= request.user)
        p_form = ProfileUpdateForm(request.POST , request.FILES ,instance= request.user.profile)
       
        
        if  u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile Update Successfull')
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance= request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)
        
        
    context = {
        'u_form' : u_form ,
        'p_form' : p_form
    }
    
    return render (request , 'profileupdate.html' , context)
    
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm 
    success_url = reverse_lazy('home')
     
    
    