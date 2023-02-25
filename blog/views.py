from django.shortcuts import render, get_object_or_404, reverse
from django.views import View, generic
from .models import Post, Comment
from .forms import CommentForm, PostForm
# return http response
from django.http import HttpResponseRedirect


# Create your views here.
# subclass ListView allows rendering a list with objects of models
class ListPost(generic.ListView):
    # filter allows only published statuses to be showen on the front end
    # - before created on allows latest post be shown
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # seperates the number of posts on the first page
    paginate_by = 8


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

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('details_post', args=[slug]))


# Add view for posting a film review
class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # lines belwo commented cause using form
    # allows all fields to be shown on page
    # fields = ('film_title','blogger', 'slug', 'director', 'actor', 'content')
