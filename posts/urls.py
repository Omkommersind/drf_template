from django.urls import path

from posts import views

urlpatterns = [
    path('api/posts', views.Post.as_view()),
    path('api/posts/<int:post_id>', views.Post.as_view()),
    path('api/posts/<int:post_id>/like', views.LikePost.as_view()),
    path('api/posts/<int:post_id>/dislike', views.DislikePost.as_view()),
]
