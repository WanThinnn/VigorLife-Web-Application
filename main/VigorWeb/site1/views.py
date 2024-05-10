from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from VigorWeb.settings import EMAIL_HOST_USER
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .forms import CommentForm
# Create your views here.
@csrf_exempt

def home(request):
    return render(request, 'site1/home.html')

def introduction(request):
    return render(request, 'site1/introduction.html')

def heallthinfo(request):
    return render(request, 'site1/heallthinfo.html')


class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')
    template_name = 'site1/heallthinfo.html'
    context_object_name = 'Posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'site1/post.html'
    
def post(request, pk, title):
    post = get_object_or_404(Post, title=title, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            parent_id = request.POST.get('parent_id')
            parent_comment = None
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.parent = parent_comment
            comment.save()
            return redirect('post', title=post.title, pk=post.pk)
    return render(request, 'site1/post.html', {'post': post, 'form': form})

def reply_comment(request, parent_id):
    parent_comment = get_object_or_404(Comment, id=parent_id)
    post = parent_comment.post
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.parent = parent_comment
            comment.save()
            return redirect('post', title=post.title, pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'site1/reply_comment.html', {'form': form})



def loseweight(request):
    return render(request, 'site1/loseweight_exercise.html')

def tools(request):
    return render(request, 'site1/tools.html')

def verifyOTP(request):
    if request.method == 'POST':
        userOTP = request.POST.get('otp')
        email=request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            form = User(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
            form.save()

        print ("OTP: ", userOTP)

    return JsonResponse({'data' : 'Hello'}, status=200)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        email=request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        form = UserCreationForm(request.POST)
        if form.is_valid():
           # form.save()
           otp = random.randint(100000,999999)
           send_mail("User Data: ", f"Your OTP is: {otp}", EMAIL_HOST_USER, [email], fail_silently=True)
           messages.success(request, 'OTP has been sent to your email')
           return render(request, 'site1/verify.html', {'otp': otp, 'first_name': first_name, 'last_name': last_name, 'email': email, 'username': user_name, 'password1': password1, 'password2': password2})
        else:
            print("Form error: ", form.errors)
            messages.error(request, form.errors)
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