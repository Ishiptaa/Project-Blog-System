from django.urls import path
from .views import BlogPostListCreate, BlogPostDetail, CommentListCreate, toggle_like

urlpatterns = [
    path('posts/', BlogPostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/like/', toggle_like, name='toggle-like'),
]

