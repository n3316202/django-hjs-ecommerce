from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# dev_7
# Create your views here.
def log_out(request):
    logout(request)
    return redirect("/")


def sign_up(request):
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get("username")
    #         raw_password = form.cleaned_data.get("password1")
    #         user = authenticate(username=username, password=raw_password)  # 사용자 인증
    #         login(request, user)  # 로그인
    #         return redirect("/")
    # else:
    #     form = UserForm()

    # return render(request, "accounts/signup.html", {"form": form})

    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],
                email=request.POST["email"],
            )
            login(request, user)
            return redirect("/")
        return render(request, "signup.html")
    return render(request, "accounts/signup.html")
