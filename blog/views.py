from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
# subclass ListView allows rendering a list with objects of models
class ListPost(generic.ListView):
    # filter allows only published statuses to be showen on the front end
    queryset = Post.objects.filter(status=1).order_by('-created_on')# - before created on allows latest post be shown
    template_name = 'index.html'

class DetailsPost(generic.DetailView):
    model = Post
    template_name = 'details_post.html'

# function to render contact form
def contact(request):
    return render(request, 'contact.html')