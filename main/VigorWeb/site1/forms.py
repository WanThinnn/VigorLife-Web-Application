from django import forms
from .models import *


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        if commit:
            comment.save()
        return comment

    class Meta:
        model = Comment
        fields = ["body"]


class RelyCommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.comment = kwargs.pop('comment', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        Reply = super().save(commit=False)
        Reply.author = self.author
        Reply.comment = self.comment
        Reply.save()

    class Meta:
        model = Reply
        fields = ["body"]


class ImageUploadForm(forms.Form):
    title = forms.CharField(label="", required=False,
                           widget=forms.TextInput
                           (attrs={
                               'class': 'blog_img',
                               'name': 'blogimg',
                               'placeholder': 'Tiêu đề ảnh',
                               'required': 'True'
                            }))
    images = forms.ImageField(required=False)
    fields = ['title']


class BlogForm(forms.ModelForm):
    title = forms.CharField(label="Tiêu đề bài viết", required=False,
                           widget= forms.TextInput
                           (attrs={
                               'class': 'blog_title',
                               'name': 'blogtitle',
                               'placeholder':'Tiêu đề...',
                               'required': 'True'
                            }))
    body = forms.CharField(label="Nội dung bài viết", required=False,
                           widget= forms.Textarea
                           (attrs={
                               'class': 'blog_body',
                               'name': 'blogbody',
                               'placeholder':'Nội dung...',
                               'required': 'True'
                            }))


    class Meta:
        model = Post
        fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        post.author = self.author

        if commit:
            post.save()  

            # Lưu các hình ảnh được cung cấp
            if self.cleaned_data.get('images'):
                images = self.cleaned_data['images']# Lấy giá trị của title từ trường ẩn image_title
                for image in images:
                    Image.objects.create(image=image, post=post)

        return post
