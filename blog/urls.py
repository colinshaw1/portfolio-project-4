from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListPost.as_view(), name='home'),
    path('<slug:slug>/', views.DetailsPost.as_view(), name='details_post'),
]
