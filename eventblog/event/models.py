from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_thumbnail = models.ImageField(upload_to="images/", null=True, blank=True)
    event_date = models.DateTimeField('Event Date & Time')
    event_location = models.CharField(max_length=400)
    event_description = models.CharField(max_length=700)

    def __str__(self):
        return self.event_name


class Suggestion(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    suggestion_date = models.DateTimeField(auto_now_add=True)
    suggestion_data = models.CharField(max_length=700)

    def __str__(self):
        return self.suggestion_data


class Feedback(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User, blank=True, null=True)
    feedback_date = models.DateTimeField(auto_now_add=True)
    feedback_data = models.CharField(max_length=700)

    def __str__(self):
        return self.feedback_data


RATING_CHOICES = (
    (' 1 ', 'One'),
    (' 2 ', 'Two'),
    (' 3 ', 'Three'),
    (' 4 ', 'Four'),
    (' 5 ', 'Five'),

)


class Rating(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)
    rating_date = models.DateTimeField(auto_now_add=True)
    rating_star = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.rating_star


class Image(models.Model):
    event = models.ForeignKey(Event)
    photo = models.ImageField(upload_to="images/event_image/", null=True, blank=True)
