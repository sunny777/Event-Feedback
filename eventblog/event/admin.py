from django.contrib import admin
from event.models import Event, Feedback, Suggestion, Rating, Image
# Register your models here.
admin.site.register(Event)
admin.site.register(Suggestion)
admin.site.register(Feedback)
admin.site.register(Rating)
admin.site.register(Image)


