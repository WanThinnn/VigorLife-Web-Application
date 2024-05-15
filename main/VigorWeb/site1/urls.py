from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('introduction/',views.introduction,name='introduction'),
    path('heallthinfo/',views.heallthinfo,name='heallthinfo'),
    path('loseweight/',views.loseweight,name='loseweight'),
    path('tools/',views.tools,name='tools'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.register,name='register'),
    path('verify/',views.verifyOTP,name='verify'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]