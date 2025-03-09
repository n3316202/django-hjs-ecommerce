from django.urls import path
from . import views

app_name = "store"

# dev_10
urlpatterns = [
    path("", views.home, name="home"),
    path("/about", views.about, name="about"),
    path("product/<int:product_id>", views.product, name="product"),  # dev_12
    path(
        "category/<str:foo>", views.category, name="category"
    ),  # 변수 foo 의 의미  참고:https://namu.wiki/w/foo #dev_13
    path("category_summary/", views.category_summary, name="category_summary"),
    # dev_21
    path("search/", views.search, name="search"),
]
