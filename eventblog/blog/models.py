from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User)
    blog_title = models.CharField(max_length=200)
    blog_body = models.CharField("Body of Blog", max_length=2500)
    created_on = models.DateTimeField(auto_now_add=True)
    overall_comment = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    user = models.ForeignKey(User, blank=True, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_data = models.CharField(max_length=700)

    def __str__(self):
        return self.comment_data


class BlogPictures(models.Model):
    blog = models.ForeignKey(Blog)
    picture = models.ImageField("Upload Picture", upload_to="images/blog/", null=True, blank=True)