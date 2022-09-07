from django.shortcuts import render
from .models import Post

# Create your views here.
# subclass ListView allows rendering a list with objects of models
class ListPost(generic.ListView):
    # filter allows only published statuses to be showen on the front end
    query = Post.objects.filter(status=1).order_by('-created_on')# - before created on allows latest post be shown
    template = 'index.html'

class DetailsPost(generic.DetailView):
    model = Post
    template = 'details_post.html'