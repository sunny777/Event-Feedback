from forms import BlogForm
from forms import CommentForm
from models import *
from models import Comment
from django.shortcuts import render_to_response
from django.contrib import messages
from django.template import RequestContext, loader
from django.db.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required(login_url='/account/login')
def blog(request):
    latest_blog_list = Blog.objects.order_by('-created_time')[:5]
    # latest_comment_list = Comment.objects.order_by('-comment_date')[:5]
    template = loader.get_template('blogs.html')
    context = RequestContext(request, {
        'latest_blog_list': latest_blog_list,
        # 'latest_comment_list':latest_comment_list,
        'template_name': 'blogs.html',
        'form_blog': BlogForm,
        'form_comment': CommentForm,
        'success_url': '/thanks/',
    })
    if request.method == 'POST':
        if 'blog_body' in request.POST:
            form = BlogForm(request.POST)
        elif 'comment_data' in request.POST:
                form = CommentForm(request.POST)
        if form.is_valid():
            blog_form = form.save(commit=False)
            if 'comment_data' in request.POST:
                blog = Blog.objects.get(id=request.POST['blog'])
                comment_count = blog.comment_set.aggregate(Count('comment_data')).values()
                if comment_count[0] != None:
                    comment_count = blog.comment_set.aggregate(Count('comment_data')).values()[0]
                else:
                    comment_count = int(request.POST['comment_data'])
                blog.overall_comment = comment_count
                blog.save()

            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            blog_form.user = User.objects.get(username=request.user)
            # Set the user object here
            blog_form.save()
            # Now you can send it to DB

    return HttpResponse(template.render(context))