from django.contrib import admin
from models import Event, Feedback, Suggestion, Rating, Image, UserProfile
# Register your models here.
admin.site.register(Event)
admin.site.register(Suggestion)
admin.site.register(Feedback)
admin.site.register(Rating)
admin.site.register(Image)
admin.site.register(UserProfile)
