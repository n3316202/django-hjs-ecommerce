from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from cart.cart import Cart
from cart.models import CartItem
from django.contrib import messages


# dev_22
# Create your views here.
def logout_user(request):
    logout(request)
    return redirect("/")


def register_user(request):
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


# dev_22
def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            saved_cart_item = CartItem.objects.filter(cart__user__id=request.user.id)

            if saved_cart_item:

                # Get the cart
                cart = Cart(request)

                for item in saved_cart_item:
                    print("===========", item.product.id)
                    print("===========", item.quantity)
                    cart.add(product=item.product, quantity=item.quantity)

            messages.success(request, "You Have been logged in")
            return redirect("/")
        else:
            messages.success(request, ("There was an error, please try again"))
            return redirect("login")
    else:
        return render(request, "accounts/login.html", {})
