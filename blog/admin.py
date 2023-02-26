from django.contrib import admin
# import from models file for post method
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Add post model using summernote admin
# summernote add a fulle feature admin editor
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('film_title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    # prepopulated fileds in admin
    prepopulated_fields = {'slug': ('film_title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    # method for approving comments
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
