from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from accounts.models import *
from dashboard.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def index(request):
    rq= user_tbl.objects.all()
    rq1=addmovie.objects.all()
    return render(request,'base/index.html',{'rq':rq,'rq1':rq1})

def sign_up(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        age = request.POST['age']
        rdate = request.POST['regdate']
        username = request.POST['username']
        password = request.POST['password']

        if len(request.FILES) != 0:
            image = request.FILES['profile']

        user2 = user_tbl(fname=fname,lname=lname,gender=gender,age=age,image=image,reg_date=rdate,username=username,password=password)

        user = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname)
        
        user.save()
        user2.save()
        
    return render(request,'base/signup.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                print("username or pass word incorect")

        cont = {}
        return render(request, 'base/login.html', cont)

def logoutPage(request):
    logout(request)
    return redirect('login')


