"""URLs for the app."""

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.urls import path

from .views import (
    get_channel_information,
    home_view,
    profile_view,
    register_view,
)

app_name = "app"

urlpatterns = [
    # authentication
    path("register/", register_view, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # home page
    path("", home_view, name="home"),
    # profile page
    path("profile/", profile_view, name="profile"),
    # scan page
    path("get-channel-information/", get_channel_information, name="get_channel_information"),
]
