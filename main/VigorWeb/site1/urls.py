from django.contrib import admin
from django.urls import path
from . import views
from .models import Post
from django.views.generic import ListView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
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
        paginate_by=1), name='blog'),
    path('<int:pk>/', views.post, name='post'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)