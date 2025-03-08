from django.urls import path
from . import views

app_name = "store"

# dev_10
urlpatterns = [
    path("", views.home, name="home"),
    path("/about", views.about, name="about"),
    path("product/<int:product_id>", views.product, name="product"), #dev_12
]
