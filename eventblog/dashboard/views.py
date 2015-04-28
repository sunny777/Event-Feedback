from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.forms import BlogForm, CommentForm
from django.views.generic.edit import FormView
from blog.models import Blog
from event.forms import FeedbackForm, SuggestionForm, RatingForm
from blog.models import Comment
from django.db.models import *
# Create your views here.


@login_required(login_url='/account/login')
def dashboard(request):
        top_ranked_events = Event.objects.order_by('-overall_rating')[:5]
        top_commented_blog = Blog.objects.order_by('-overall_comment')[:5]
        my_blogs = Blog.objects.filter(user=User.objects.get(username=request.user))
        trending_event = Event.objects.order_by('-event_date')[:2]
        trending_blog = Blog.objects.order_by('-created_date')[:3]
        template = loader.get_template('dashboard.html')
        context = RequestContext(request, {
            'top_ranked_events': top_ranked_events,
            'top_commented_blog': top_commented_blog,
            'my_blogs': my_blogs,
            'trending_event': trending_event,
            'trending_blog': trending_blog,
            'form_class': BlogForm,
            'form_feedback': FeedbackForm,
            'form_suggestion': SuggestionForm,
            'form_rating': RatingForm,
            'form_comment': CommentForm,
            'template_name': 'dashboard.html',
            'success_url': '/thanks/',
        })
        if request.method == 'POST':
            if 'blog_body' in request.POST:
                form = BlogForm(request.POST)
            elif 'feedback_data' in request.POST:
                form = FeedbackForm(request.POST)
            elif 'suggestion_data' in request.POST:
                form = SuggestionForm(request.POST)
            elif 'rating_star' in request.POST:
                form = RatingForm(request.POST)
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
                elif 'rating_star' in request.POST:
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

                blog_form.user = User.objects.get(username=request.user) # Set the user object here
                blog_form.save() # Now you can send it to DB

        return HttpResponse(template.render(context))