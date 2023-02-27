from . import views
from django.urls import path


urlpatterns = [
    # '' represents empty string and returns an result from ListPost
    path('', views.ListPost.as_view(), name='home'),
    path('add_post/', views.AddPostView.as_view(), name="add_post"),
    # <slug> in the brackets captures the values from the url and returns the post details
    path('<slug:slug>/', views.PostDetail.as_view(), name='details_post'),
    path('<slug:slug>/edit', views.EditPost.as_view(), name='edit_post'),
    path('<slug:slug>/delete', views.DeletePost.as_view(), name='delete'),
    path('likes/<slug:slug>', views.PostLike.as_view(), name="post_like"),
    # path('<slug:slug>/delete_comment', views.DeleteComment, name='delete_comment'),
    
]
