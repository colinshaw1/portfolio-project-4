from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# declaring tuples to be able to post drafts and publish posts
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


#create class for contact models 
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    def __str__(self):
        return self.name


# class for posting data to databse with approriate information
class Post(models.Model):
    film_title = models.CharField(max_length=200, unique=True, null=True) 
    slug = models.SlugField(max_length=200, unique=True, null=True)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True)
    director = models.CharField(max_length=200, unique=True, null=True)
    actor = models.CharField(max_length=200, unique=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    content = models.TextField()
    # results are sorted in order of created on from meta class
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)



    # meta class to order and sort results in order of created 
    # on so most recent posts show first
    class Meta:
        ordering = ['-created_on']

    # string class to read title representation in adminsitration site
    def __str__(self):
        return self.film_title

#class for commetns model to post with correct infromation
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        logging.error(self)
        return self.body
        