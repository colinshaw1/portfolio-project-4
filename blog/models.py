from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#declaring tuples to be able to post drafts and publish posts
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# class for posting data to databse with approriate information
class Post(models):
    film_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    director = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    actor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    #results are sorted in order of created on from meta class
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices==STATUS, default=0)
