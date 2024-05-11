from django.contrib import admin
from .models import Post, Image
from .models import Post, Comment
# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'date' ]
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]
    def get_parent_title(self, obj):
        if obj.parent:
            return obj.parent.title
        return None

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_date', 'post')
    raw_id_fields = ('post',)  # Cho phép nhập ID của bài đăng thay vì sử dụng giao diện chọn
    
    def post_date(self, obj):
        return obj.post.date if obj.post else None
    post_date.short_description = 'Post Date'
admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
