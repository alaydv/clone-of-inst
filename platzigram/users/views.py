from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post

# Forms
from users.forms import SignupForm
from users.models import Profile


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    User Detail View
    """
    template_name = 'users/detail.html'
    slug_field: str = 'username'
    slug_url_kwarg: str = 'username'
    queryset = User.objects.all()
    context_object_name: str = 'user'

    def get_context_data(self, **kwargs):
        """Add users posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignupView(FormView):
    """
    Sign up view
    """
    template_name: str = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save data"""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """
    Update view for an acount
    """
    template_name: str = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """
    Login View
    """
    template_name: str = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """
    Logout View
    """
    template_name: str = 'users/login.html'