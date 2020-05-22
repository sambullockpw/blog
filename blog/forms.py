from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    photo = forms.FileField()
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)