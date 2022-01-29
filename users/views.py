from django.shortcuts import redirect, render
from django.contrib.auth import login , authenticate, logout
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successfull')
            return redirect('home')
    
    else:
        form = RegisterForm()
        
 
    return render(request, "registration.html" , {'form' : form})


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            
            user = authenticate(request,username=username , password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfull')
                return redirect("home")
            else:
                messages.error(request, 'Username or Password is incorrect')
                
        else:
            messages.error(request, 'Fill out all the fills')
                
    return render(request, "login.html")

    

def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Log out Successfull')
        return redirect('/')
    
    else:
        return redirect('login')
    
    
    

    
