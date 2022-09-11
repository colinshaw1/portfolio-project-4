from . import views
from django.urls import path

urlpatterns = [
    # '' represents empty string and returns an result from ListPost
    path('', views.ListPost.as_view(), name='home'),
    # <slug> in the brackets captures the values from the url and returns the post details
    path('<slug:slug>/', views.DetailsPost.as_view(), name='details_post'),
    # create path for contact form
    path('', views.contact, name='contact'),
]
