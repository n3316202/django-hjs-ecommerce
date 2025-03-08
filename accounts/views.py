from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


# dev_7
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect("/")
