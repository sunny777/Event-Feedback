from django.contrib import admin
from models import Blog, Comment


class CommentAdmin(admin.TabularInline):
    model = Comment
    fields = ('comment_data', 'user')
    extra = 0
    readonly_fields = ('user',)


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    inlines = (CommentAdmin,)
    date_hierarchy = 'created_date'
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

