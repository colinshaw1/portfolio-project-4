from django.contrib import admin
#import from models file for post method
from .models import Post

# Register your models here.
admin.site.register(Post)