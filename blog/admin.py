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

# # add class for making admin dashbord have filters, searchs and list fileds using djangos bnuilt in methods
# class PostAdmin(admin.ModelAdmin):
#     # atribute displays the properties below
#     list_display = ('film_title', 'slug', 'status', 'created_on')
#     # attribute to filter the psots by there status
#     list_filter = ('status',)
#     # attribute to search the database for film titles and content
#     search_fields = ['film_title', 'content']
#     # attribute to populate the slug
#     prepopulated_fields = {'slug': ('film_title',)}

# # registers the comments into admin area


# @admin.register(Comment)
# # class to customise the representation of data
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)


# # @admin.register(Contact)
# # class ContactAdmin(admin.ModelAdmin):
# #     list_display = ('email', 'name')

# #     def approve_email(self, request, queryset):
# #         queryset.update(active=True)

# Register your models here.
# admin.site.register(Post)
