from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from store.models import Product


# Create your views here.
# dev_5
def home(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})
