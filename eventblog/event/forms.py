__author__ = 'User'

from django.forms import *    # fill in custom user info then save it
from models import Feedback
from models import Suggestion
from models import Rating
from django.core.files.images import get_image_dimensions
from models import UserProfile
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        # exclude = ('event_id',)
        fields = ('feedback_data', 'event')
        labels = {
            'feedback_data': "",
            'event': "",
        }
        widgets = {
            'feedback_data': TextInput(attrs={'class': 'form-control', 'placeholder': 'Give feedback...'}),
            'event': TextInput(attrs={'style': 'display:none;'}),
        }


class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        fields = ('suggestion_data', 'event')
        labels = {
            'suggestion_data': "",
            'event': "",
        }
        widgets = {
            'suggestion_data': TextInput(attrs={'class': 'form-control', 'placeholder': 'Give suggestion...'}),
            'event': TextInput(attrs={'style': 'display:none;'}),
        }


RATING_CHOICES = (
    (' 0 ', 'Select Ratings'),
    (' 1 ', '*'),
    (' 2 ', '**'),
    (' 3 ', '***'),
    (' 4 ', '****'),
    (' 5 ', '*****'),

)


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ('rating_star', 'event')
        labels = {
            'rating_star': "",
            'event': "",
        }
        widgets = {
            'rating_star': Select(choices=RATING_CHOICES, attrs={'class': 'form-control'}),
            'event': TextInput(attrs={'style': 'display:none;'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_picture', 'user_gender')
