from django.urls import path
from .views import PostListView, PostDetailView, CategoryListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryListView.as_view(),name='category_posts'),
]