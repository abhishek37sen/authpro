from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from dairy.views import show


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method=="POST":
        if request.POST['password']==request.POST['passwordagain']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': "Username already Has been taken"})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['passwordagain'])
                return redirect(home)
        else:
            return render(request,'register.html',{'error':"Password don't match"})
    else:
        return render(request, 'register.html')




def login(request):
    if request.method == "POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect(show)
        else:
            return render(request,'home.html',{'error':"invalid login id..."})
    else:
        return render(request, 'home.html')



def logout(request):
    auth.logout(request)
    return redirect(home)