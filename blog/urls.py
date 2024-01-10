from django.urls import path

# importing from the same directory level
from . import views

urlpatterns = [
    # dynamic segment
    path("", views.home, name="home"),
    path("/posts", views.posts, name="posts"),
    path("/posts/<slug:slug>", views.post_by_slug, name="posts-by-slug"),
]
