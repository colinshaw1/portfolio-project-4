from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post,  Comment
from .forms import CommentForm
# return http response
from django.http import HttpResponse


# Create your views here.
# subclass ListView allows rendering a list with objects of models
class ListPost(generic.ListView):
    # filter allows only published statuses to be showen on the front end
    # - before created on allows latest post be shown
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # seperates the number of posts on the first page
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        # gets the comments attached to a post
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        # check if liked post by user id
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "details_post.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    # same as get method above
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # creating a new variable called commentform
        comment_form = CommentForm(data=request.POST)
        # gets the data from the form
        # see if the user leaving the comment is valid
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "details_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

# def details_post(request, slug):
#     template_name = 'details_post.html'
#     post = get_object_or_404(Post, slug=slug)
#     # comments = get_object_or_404(Comment, slug=slug)
#     comment = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':

#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'post': post,
#                                            'comments': comment,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})


# # class contact_post(generic.DetailView):
# #     template_name = 'about.html'
# #     model = CommentForm
