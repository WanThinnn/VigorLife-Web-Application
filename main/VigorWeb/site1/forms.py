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

class BlogForm(forms.ModelForm):
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
        return post