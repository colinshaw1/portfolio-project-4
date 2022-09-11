from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Contact, Comment
from .forms import CommentForm
import logging


# return http response
from django.http import HttpResponse


# Create your views here.
# subclass ListView allows rendering a list with objects of models
class ListPost(generic.ListView):
    # filter allows only published statuses to be showen on the front end
    # - before created on allows latest post be shown
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'



class DetailsPost(generic.DetailView):
    model = Post
    template_name = 'details_post.html'

# function to render contact form
def Contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name
        contact.email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("<h1>Thank you for contacting Film Blog</h1>")

    return render(request, 'contact.html')

def details_post(request, slug):
    logging.error('here')
    template_name = 'details_post.html'
    post = get_object_or_404(Post, slug=slug)
    # comments = get_object_or_404(Comment, slug=slug)
    comment = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comment,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
