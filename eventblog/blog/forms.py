__author__ = 'User'

from django.forms import *    # fill in custom user info then save it
from models import Blog
from models import Comment
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
            'blog_title': TextInput(attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Give a title to your blog..' }),
            'blog_body': Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': 'True', 'placeholder': 'Write content for your blog..' }),
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
            'comment_data': TextInput(attrs={'class': 'form-control', 'placeholder': 'Give your comments...', 'required': 'True', }),
            'blog': TextInput(attrs={'style': 'display:none;'}),
        }