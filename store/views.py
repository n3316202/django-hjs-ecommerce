from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
# dev_1
def home(request):

    return HttpResponse("<h1>안녕하세요<h1>")
