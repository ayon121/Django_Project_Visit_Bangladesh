from django.shortcuts import render

from .models import Destination ,Testimonials , NewPosts,NewsSidebar ,IntroItem ,Footer

# Create your views here.
# Create your views here.
def home(request):
    dests = Destination.objects.all()
    testi = Testimonials.objects.all()
    posts =  NewPosts.objects.all()
    newssidebar = NewsSidebar.objects.all()
    items = IntroItem.objects.all()
    foots = Footer.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        username = current_user.username
        return render(request, "home.html" ,{ 'dests': dests ,'testi': testi , 'posts' : posts , 'news' : newssidebar , 'items' : items , 'foot' : foots , 'user_name' : username})

    else:
        return render(request, "home.html" ,{ 'dests': dests ,'testi': testi , 'posts' : posts , 'news' : newssidebar , 'items' : items , 'foot' : foots})




def search_Destination(request):
    if request.method == 'POST':
        searched = request.POST.get('searched') 
        destination = Destination.objects.filter(name__contains=searched) 
        
        searchedprice = request.POST.get('searchedprice') 
        destinationprice = Destination.objects.filter(price__contains=searchedprice)   
        return render(request, "search.html" , {'searched' : searched , 'destination' : destination , 'searchedprice':searchedprice  , 'destinationprice': destinationprice})
        
    else:   
        return render(request, "search.html" )


