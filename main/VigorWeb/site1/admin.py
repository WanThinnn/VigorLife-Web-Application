from django.contrib import admin
from .models import *
# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment


class ReplyCommentInline(admin.StackedInline):
    model = Reply


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]

    def get_parent_title(self, obj):
        if obj.parent:
            return obj.parent.title
        return None


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_date', 'post')
    # Cho phép nhập ID của bài đăng thay vì sử dụng giao diện chọn
    raw_id_fields = ('post',)
    search_fields = ['post', 'title']
    list_filter = ['post']

    def post_date(self, obj):
        return obj.post.date if obj.post else None
    post_date.short_description = 'Post Date'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post']
    list_filter = ['date']
    search_fields = ['author']
    inlines = [ReplyCommentInline]


class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'display_comment_post', 'date']
    list_filter = ['date']
    search_fields = ['author']

    def display_comment_post(self, obj):
        return f'{obj.comment.post.title} - {obj.comment.body}'
    display_comment_post.short_description = 'Post and Comment'


class FruitAdmin(admin.ModelAdmin):
    list_display = ['name', 'classification', 'calories']
    list_filter = ['name']
    search_fields = ['name', 'classification']


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'classification', 'calories', 'unit']
    list_filter = ['name']
    search_fields = ['name', 'classification']


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'link',
                    'description_text', 'image', 'type']
    list_filter = ['pub_date', 'type']
    search_fields = ['title', 'pub_date', 'type']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyCommentAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Fruit, FruitAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
