from django.contrib import admin
#import from models file for post method
from .models import Post


# add class for making admin dashbord have filters, searchs and list fileds using djangos bnuilt in methods
class PostAdmin(admin.ModelAdmin):
    list_display = ('film_title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['film_title', 'content']
    prepopulated_fields = {'slug':('film_title',)}

# Register your models here.
admin.site.register(Post, PostAdmin)