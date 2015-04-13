from django.shortcuts import render
from blog.forms import BlogForm
from event.forms import FeedbackForm
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
            'form_class': FeedbackForm,
            'template_name': 'events.html',
            'success_url': '/thanks/',
        })
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                events = form.save(commit=False)
                    # commit=False tells Django that "Don't send this to database yet.
                    # I have more things I want to do with it."

                events.user = User.objects.get(username=request.user)
                print request.POST
                events.event = Event.objects.get(id=3)
                # Set the user object here
                events.save()
                # Now you can send it to DB

        return HttpResponse(template.render(context))