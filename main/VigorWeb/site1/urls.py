from django.contrib import admin
from django.urls import path, include
from . import views
from .models import *
from django.views.generic import ListView
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .views import ImageUploadView

urlpatterns = [
#     path('',views.home,name='home'),
#     path('introduction/',views.introduction,name='introduction'),
#     path('heallthinfo/',views.heallthinfo,name='heallthinfo'),
#     path('loseweight/',views.loseweight,name='loseweight'),
#     path('tools/',views.tools,name='tools'),
#     path('login/',views.loginPage,name='login'),
#     path('logout/',views.logoutPage,name='logout'),
#     path('register/',views.register,name='register'),
#     path('verify/',views.verifyOTP,name='verify'),
#     path('social-auth/', include('social_django.urls', namespace='social')),
# ]
    path('', views.home, name='home'),
    path('introduction/', views.introduction, name='introduction'),
    # path('blog/',views.heallthinfo,name='blog'),
    path('loseweight/', views.loseweight, name='loseweight'),
    path('autosuggest/', autosuggest, name='autosuggest'),
    path('search/', views.search, name='search'),
    path('calo/', views.calo, name='calo'),
    path('tools/', views.tools, name='tools'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('verify/', views.verifyOTP, name='verify'),
    path('ver/', views.verify, name='ver'),
    path('account/', views.account, name='account'),
    path('forgot-password/', views.forgotpass, name='forgot'),
    path('change-password/', views.changepass, name='changepass'),
    
    path('blog/', ListView.as_view(
        queryset=Post.objects.all().order_by('-date'),
        template_name='site1/blog.html',
        context_object_name='Posts',
        paginate_by=10), name='blog'),
    path('<int:pk>-<str:title>/', views.post, name='post'),
    path('reply/<int:pk>-<str:title>/', views.reply_cmt, name='reply'),
    path('blog/write_blog/', views.write_blog, name='write_blog'),
    
    path('fruits/', views.ListFruit, name='list-fruits'),
    path('fruits/<str:classification>/', FruitListView.as_view(), name='fruits'),
    path('fruits/<str:classification>/<str:name>',views.FruitsPage, name='fruitspage'),
    
    path('foods/', views.ListFoods, name='list-foods'),
    path('foods/<str:classification>/', FoodListView.as_view(), name='foods'),
    path('foods/<str:classification>/<str:name>', views.FoodsPage, name='foodspage'),
    
    path('news/<str:type>/', views.News, name='news'), 
    path('news/', views.ListNews, name='list-news'), 
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('upload/', ImageUploadView.as_view(), name='upload'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
