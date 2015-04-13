from blog.forms import *
from models import Blog
from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from django.template import RequestContext, loader
from event.models import Event
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required(login_url='/account/login')
def blog(request):
    if request.method == 'POST':
        if 'BlogForm' in request.POST:
            form = BlogForm(request.POST)
        elif 'comment_data' in request.POST:
                form = CommentForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."

            blog.user = User.objects.get(username=request.user) # Set the user object here
            blog.save() # Now you can send it to DB
    latest_blog_list = Blog.objects.order_by('-created_on')[:5]
    template = loader.get_template('blogs.html')
    context = RequestContext(request, {
        'latest_blog_list': latest_blog_list,
        'template_name': 'blogs.html',
        'form_blog': BlogForm,
        'form_comment': CommentForm,
        'success_url': '/thanks/',
    })
    return HttpResponse(template.render(context))
