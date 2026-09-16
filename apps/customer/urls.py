from django.urls import path
from apps.customer.views import login_view, main_page_view, signup_view

urlpatterns = [
    path("", main_page_view, name="home"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
]