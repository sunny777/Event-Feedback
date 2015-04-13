from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.forms import BlogForm
from django.views.generic.edit import FormView
from event.models import Event
from blog.models import Blog
# Create your views here.


@login_required(login_url='/account/login')
def dashboard(request):
        latest_event_list = Event.objects.order_by('-event_date')[:5]
        latest_blog_list = Blog.objects.order_by('-created_on')[:5]
        template = loader.get_template('dashboard.html')
        context = RequestContext(request, {
            'latest_event_list': latest_event_list,
            'latest_blog_list': latest_blog_list,
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



