from django import forms
from .models import *
import re
from django.contrib.auth.models import User

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

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^[\w]+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email đã tồn tại")
        return email
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])