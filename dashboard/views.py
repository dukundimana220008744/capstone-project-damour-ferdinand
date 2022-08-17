from django.shortcuts import render,redirect
from dashboard.models import *
from django.contrib.auth import authenticate, login, logout
from accounts.models import *
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    us=user_tbl.objects.filter(username=request.user)
    if 's' in request.GET:
        s=request.GET['s']
        movies=addmovie.objects.filter(title__contains=s)
    else:
        movies=addmovie.objects.all()
    
    return render(request,'base/admin.html',{'movies':movies,'us':us})
def add(request):
  
    return render(request,'base/basic-form.html')
def addMovie(request):
    if request.method=='POST':
        title=request.POST['title']
        actor=request.POST['actor']
        trailer=request.POST['trailer']
        realesddate=request.POST['Rdate']
        poster=request.POST['poster']
        username=request.POST['user']
        genre=request.POST['genre']
        description=request.POST['description']
        images=request.FILES['images']
    movie=addmovie(title=title,actor=actor,trailer=trailer,poster=poster,user=username,realeseddate=realesddate,genre=genre,images=images)
    movie.save()
    return redirect('/dashboard')
def logoutPage(request):
    logout(request)
    return redirect('login')