from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.forms import BlogForm
from django.views.generic.edit import FormView
from blog.models import Blog
from blog.models import Comment
from django.db.models import *
# Create your views here.


@login_required(login_url='/account/login')
def dashboard(request):
        top_ranked_events = Event.objects.order_by('-overall_rating')[:5]
        top_commented_blog = Blog.objects.order_by('-overall_comment')[:5]
        my_blogs = Blog.objects.filter(user=User.objects.get(username=request.user))
        template = loader.get_template('dashboard.html')
        context = RequestContext(request, {
            'top_ranked_events': top_ranked_events,
            'top_commented_blog': top_commented_blog,
            'my_blogs': my_blogs,
            'form_class': BlogForm,
            'template_name': 'dashboard.html',
            'success_url': '/thanks/',
        })
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                blog = form.save(commit=False)
                # commit=False tells Django that "Don't send this to database yet.
                # I have more things I want to do with it."

                blog.user = User.objects.get(username=request.user) # Set the user object here
                blog.save() # Now you can send it to DB

        return HttpResponse(template.render(context))