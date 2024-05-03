from django.shortcuts import render

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
