from django.contrib.auth import login, views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from aimtravel_project.user_auth.forms import SignUpForm


class SignUpView(views.CreateView):
    template_name = 'user_auth/register-page.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'user_auth/sign-in.html'
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    template_name = 'user_auth/sign-out.html'


def auth_option(request):
    return render(request, template_name='user_auth/auth_page.html')
