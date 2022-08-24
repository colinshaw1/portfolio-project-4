from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# declaring tuples to be able to post drafts and publish posts
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# class for posting data to databse with approriate information
class Post(models.Model):
    film_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    director = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts_director')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts_actor')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    # results are sorted in order of created on from meta class
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # meta class to order and sort results in order of created 
    # on so most recent posts show first
    class Meta:
        ordering = ['-created_on']

    # string class to read title representation in adminsitration site
    def __str__(self):
        return self.title
