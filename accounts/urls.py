from django.contrib import admin
from django.urls import include, path

from django.contrib.auth import views as auth_views

from accounts import views

# dev_7
app_name = "accounts"

urlpatterns = [
    # django.contrib.auth앱의 LoginView 클래스를 활용했으므로 별도의 views.py 파일 수정이 필요 없음
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", views.log_out, name="logout"),  # 코드 추가하기
    path("signup/", views.sign_up, name="signup"), 
]
