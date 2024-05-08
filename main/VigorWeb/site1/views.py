from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'site1/home.html')

def introduction(request):
    return render(request, 'site1/introduction.html')

def heallthinfo(request):
    return render(request, 'site1/heallthinfo.html')

def loseweight(request):
    return render(request, 'site1/loseweight_exercise.html')

def tools(request):
    return render(request, 'site1/tools.html')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'site1/register.html',context)
  
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    context = {}
    return render(request, 'site1/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')