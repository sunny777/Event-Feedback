from django.contrib import admin
from models import Event, Feedback, Suggestion, Rating, Image, UserProfile

# Register your models here.


class FeedbackAdmin(admin.TabularInline):
    model = Feedback
    fields = ('feedback_data', 'user')
    extra = 0
    #readonly_fields = ('user',)


class SuggestionAdmin(admin.TabularInline):
    model = Suggestion
    fields = ('suggestion_data', 'user')
    extra = 0
    #readonly_fields = ('user',)


class RatingAdmin(admin.TabularInline):
    model = Rating
    fields = ('rating_star', 'user')
    extra = 0
    #readonly_fields = ('user',)


class EventAdmin(admin.ModelAdmin):
    model = Event
    inlines = (FeedbackAdmin, SuggestionAdmin, RatingAdmin, )
    date_hierarchy = 'event_date'


admin.site.register(Event, EventAdmin)
admin.site.register(Feedback)
admin.site.register(Suggestion)
admin.site.register(Rating)
admin.site.register(Image)
admin.site.register(UserProfile)
