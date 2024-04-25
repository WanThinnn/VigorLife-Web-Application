from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('introduction/',views.introduction,name='introduction'),
    path('heallthinfo/',views.heallthinfo,name='heallthinfo'),
    path('loseweight/',views.loseweight,name='loseweight'),
]