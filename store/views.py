from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
# dev_4
def home(request):
    return render(request, "store/home.html", {})
