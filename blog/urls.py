from . import views
from django.urls import path


urlpatterns = [
    # '' represents empty string and returns an result from ListPost
    path('', views.ListPost.as_view(), name='home'),
    # # <slug> in the brackets captures the values from the url and returns the post details
    # path('<slug:slug>/', views.DetailsPost.as_view(), name='details_post'),
    # path('<slug:slug>/', views.details_post, name='comments'),
    # # path('<slug:slug>/', views.ListComment.as_view(), name='details_post'),
    # path('<slug:slug>/comment', views.details_post, name='comment'),
    # # create path for contact form
    # # path('<slug:slug>/Contact', views.Contact, name='about'),
]
