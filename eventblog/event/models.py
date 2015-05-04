from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models import signals
from notification import models as notification

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_thumbnail = models.ImageField(upload_to="images/", null=True, blank=True)
    event_date = models.DateField('Event Date')
    event_time = models.TimeField('Event Time')
    event_location = models.CharField(max_length=400)
    event_description = models.CharField(max_length=700)
    overall_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.event_name


class Suggestion(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    suggestion_date = models.DateField(auto_now_add=True)
    suggestion_time = models.TimeField(auto_now_add=True)
    suggestion_data = models.CharField(max_length=700)

    def __str__(self):
        return self.suggestion_data


class Feedback(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User, blank=True, null=True)
    feedback_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    feedback_data = models.CharField(max_length=700)

    def __str__(self):
        return self.feedback_data


class Rating(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    rating_date = models.DateField(auto_now_add=True)
    rating_time = models.TimeField(auto_now_add=True)
    rating_star = models.FloatField(null=True)

    def __unicode__(self):
        return self.event.event_name


class Image(models.Model):
    event = models.ForeignKey(Event)
    photo = models.ImageField(upload_to="images/event_image/", null=True, blank=True)

    def __unicode__(self):
        return self.event.event_name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_picture = models.ImageField(upload_to="images/", null=True, blank=True)
    user_gender = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.user.username



