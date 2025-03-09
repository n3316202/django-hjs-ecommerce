from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from cart import views
from django.conf.urls.static import static

app_name = "cart"  # dev_14

urlpatterns = [
    path("", views.cart_summary, name="cart_summary"),
    path("add/", views.cart_add, name="cart_add"),
    path("delete/", views.cart_delete, name="cart_delete"),
    path("update/", views.cart_update, name="cart_update"),
]
