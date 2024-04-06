from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('index/',views.index,name='index'),
    path('tool/',views.tool,name='tool'),
    path('introduction/',views.introduction,name='introduction'),
    path('healthinfo/',views.healthinfo,name='healthinfo'),
    path('loseweight/',views.loseweight,name='loseweight'),
]