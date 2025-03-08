from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
# dev_1
def home(request):

    return HttpResponse("<h1>이제부터 쇼핑몰을 만들어 보자</h1>")
