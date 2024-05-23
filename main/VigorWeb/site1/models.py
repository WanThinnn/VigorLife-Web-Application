from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from datetime import datetime
# Create your models here.


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post_image = models.ForeignKey(
        'Image', on_delete=models.SET_NULL, null=True, related_name='post_images')

    def __str__(self):
        return self.title

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='post_images/')
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Image for {self.post.date} - {self.post.title}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Replied by {self.author} for {self.comment}'


class Fruit(models.Model):
    CLASSIFICATION_CHOICES = [
        ('high_calories', 'Nhiều Calo'),
        ('low_calories', 'Ít Calo'),
        ('medium_calories', 'Calo Vừa Phải'),
    ]
    name = models.CharField(max_length=100)  # Tên của trái cây
    description = models.TextField()         # Mô tả trái cây
    calories = models.IntegerField()         # Lượng calo của trái cây
    classification = models.CharField(
        max_length=50, choices=CLASSIFICATION_CHOICES)  # Phân loại trái cây
    # Hình ảnh của trái cây
    image = models.ImageField(upload_to='fruit_images/')

    def __str__(self):
        return self.name


class Food(models.Model):
    CLASSIFICATION_CHOICES = [
        ('high_calories', 'Nhiều Calo'),
        ('low_calories', 'Ít Calo'),
        ('medium_calories', 'Calo Vừa Phải'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()
    unit = models.CharField(max_length=50, null=True)
    classification = models.CharField(
        max_length=50, choices=CLASSIFICATION_CHOICES)
    # Hình ảnh của trái cây
    image = models.ImageField(upload_to='foods_images/')

    def __str__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    # Ensure unique links to avoid duplicates
    link = models.URLField(unique=True)
    description_text = models.TextField()
    image = models.URLField()
    type = models.CharField(max_length=50, null=True)  # Thêm trường type

    def __str__(self):
        return self.title
