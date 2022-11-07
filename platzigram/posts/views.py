from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


class PostsFeedView(LoginRequiredMixin, ListView):
    """Returned all published posts"""
    template_name: str = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by: int = 30
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Returned a specific post"""
    template_name: str = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name: str = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create a new view"""
    template_name: str = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile context"""
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context
