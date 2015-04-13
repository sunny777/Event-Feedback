from django.shortcuts import render
from blog.forms import BlogForm
from event.forms import *
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext, loader
from models import Event
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/account/login')
def event(request):
        latest_event_list = Event.objects.order_by('-event_date')[:5]
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
                events = form.save(commit=False)
                    # commit=False tells Django that "Don't send this to database yet.
                    # I have more things I want to do with it."

                events.user = User.objects.get(username=request.user)
                # Set the user object here
                events.save()
                # Now you can send it to DB

        return HttpResponse(template.render(context))