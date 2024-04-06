from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def index(request):
    return render(request, 'app/index.html')

def tool(request):
    return render(request, 'app/tool.html')

def introduction(request):
    return render(request, 'app/introduction.html')

def loseweight(request):
    return render(request, 'app/loseweight_exercise.html')

def healthinfo(request):
    return render(request, 'app/healthinfo.html')



def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'app/register.html',context)
  
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
    return render(request, 'app/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('index')
    
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password') 
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             messages.info(request, 'Username or Password is incorrect')
    
#     context = {}
#     return render(request, 'app/login.html', context)