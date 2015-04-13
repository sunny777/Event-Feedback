__author__ = 'User'

from django.forms import *    # fill in custom user info then save it
from blog.models import Blog
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
