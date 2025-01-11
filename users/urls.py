from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="/blogs/"), name="logout"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
]
