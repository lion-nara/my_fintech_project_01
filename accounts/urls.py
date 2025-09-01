# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/",  auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="accounts:login"), name="logout"),
    # 선택: 회원가입을 쓸 거면 아래 줄 살리고, 안 쓸 거면 지워도 됨
    path("signup/", views.signup, name="signup"),
]