from django.contrib import admin
from .models import Post, Image
from .models import Post, Comment
# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]

class ListImages(admin.ModelAdmin):
    list_display = ['id','post']
    search_fields = ['title']
 
admin.site.register(Post, PostAdmin)
admin.site.register(Image, ListImages)
