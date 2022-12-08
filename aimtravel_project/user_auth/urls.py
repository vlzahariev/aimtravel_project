from django.contrib.auth.views import PasswordChangeView
from django.urls import path
from . import views

from aimtravel_project.user_auth.views import SignUpView, SignInView, SignOutView, auth_option

urlpatterns = (
    path('', auth_option, name='auth option'),
    path('register/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('change_password/', PasswordChangeView.as_view(template_name='user_auth/change-password.html', success_url='/'), name='change password'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
)
