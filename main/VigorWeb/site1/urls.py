from django.contrib import admin
from django.urls import path
from . import views
from .models import *
from django.views.generic import ListView
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.autocomplete, name='autocomplete'),
    path('introduction/', views.introduction, name='introduction'),
    # path('blog/',views.heallthinfo,name='blog'),
    path('loseweight/', views.loseweight, name='loseweight'),
    path('tools/', views.tools, name='tools'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('verify/', views.verifyOTP, name='verify'),
    path('blog/', ListView.as_view(
        queryset=Post.objects.all().order_by('-date'),
        template_name='site1/blog.html',
        context_object_name='Posts',
        paginate_by=10), name='blog'),
    path('<int:pk>-<str:title>/', views.post, name='post'),
    path('reply/<int:pk>-<str:title>/', views.reply_cmt, name='reply'),
    path('blog/write_blog/', views.write_blog, name='write_blog'),
    path('fruits/<str:classification>/', FruitListView.as_view(), name='fruits'),
    path('fruits/', views.ListFruit, name='list-fruits'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
