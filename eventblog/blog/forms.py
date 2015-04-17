__author__ = 'User'

from django.forms import *    # fill in custom user info then save it
from blog.models import Blog
from blog.models import Comment
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_body')
        labels = {
            'blog_title': _('Title'),
            'blog_body': _('Blog Description'),
        }
        widgets = {
            'blog_title': TextInput(attrs={'class': 'form-control'}),
            'blog_body': Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_data', 'blog')
        labels = {
            'comment_data': "",
            'blog': "",
        }
        widgets = {
            'comment_data': TextInput(attrs={'class': 'form-control', 'placeholder': 'Give your comments...'}),
            'blog': TextInput(attrs={'style': 'display:none;'}),
        }