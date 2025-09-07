from django.views.generic import ListView, DetailView
from unicodedata import category

from .models import Category, Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class CategoryListView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        return Post.objects.filter(category__slug=category_slug, is_published=True).order_by('created_at')

