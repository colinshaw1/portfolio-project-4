from django.contrib import admin
#import from models file for post method
from .models import Post, Contact


# add class for making admin dashbord have filters, searchs and list fileds using djangos bnuilt in methods
class PostAdmin(admin.ModelAdmin):
    # atribute displays the properties below
    list_display = ('film_title', 'slug', 'status', 'created_on')
    # attribute to filter the psots by there status
    list_filter = ('status',)
    # attribute to search the database for film titles and content
    search_fields = ['film_title', 'content']
    # attribute to populate the slug
    prepopulated_fields = {'slug':('film_title',)}

# Register your models here.
admin.site.register(Post, PostAdmin, Contact)