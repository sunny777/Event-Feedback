from django.shortcuts import render
from blog.forms import BlogForm
from event.forms import *
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext, loader
from models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime, time
from django.db.models import Avg
# Create your views here.

@login_required(login_url='/account/login')
def event(request, id=None):
   if id != None:
       latest_event_list = Event.objects.filter(id=id)
   else:
       latest_event_list = Event.objects.order_by('-event_date')
   template = loader.get_template('events.html')
   context = RequestContext(request, {
       'latest_event_list': latest_event_list,
       'form_feedback': FeedbackForm,
       'form_suggestion': SuggestionForm,
       'form_rating': RatingForm,
       'template_name': 'events.html',
       'success_url': '/thanks/',
   })
   if request.method == 'POST':
       if 'feedback_data' in request.POST:
           form = FeedbackForm(request.POST)
       elif 'suggestion_data' in request.POST:
           form = SuggestionForm(request.POST)
       elif 'rating_star' in request.POST:
           form = RatingForm(request.POST)
       if form.is_valid():
           new_form = form.save(commit=False)
           if 'rating_star' in request.POST:
               event = Event.objects.get(id=request.POST['event'])
               stars_average = event.rating_set.aggregate(Avg('rating_star')).values()
               if stars_average[0] != None:
                   stars_average = event.rating_set.aggregate(Avg('rating_star')).values()[0]
               else:
                   stars_average = float(request.POST['rating_star'])
               event.overall_rating = stars_average
               event.save()
               # commit=False tells Django that "Don't send this to database yet.
               # I have more things I want to do with it."

           new_form.user = User.objects.get(username=request.user)
           # Set the user object here
           new_form.save()
           # Now you can send it to DB
   return HttpResponse(template.render(context))