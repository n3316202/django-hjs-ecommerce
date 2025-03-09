from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from store.models import Category, Product
from django.contrib import messages
from django.db.models import Q


# Create your views here.
# dev_5
def home(request):
    products = Product.objects.all()
    # dev_13
    categories = Category.objects.all()
    return render(
        request, "store/home.html", {"products": products, "categories": categories}
    )


# dev_10
def about(request):
    return render(request, "store/about.html", {})
    # return render(request, "orders/checkout.html", {})


# dev_12
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "store/product.html", {"product": product})


def category(request, foo):
    # Replace Hyphens with Spaces

    foo = foo.replace("-", " ")
    # print(foo)

    # Grab the category from the url
    try:
        # Look up the category
        category = Category.objects.get(name=foo)
        print(category)

        products = Product.objects.filter(category=category)
        print(products)

        return render(
            request,
            "store/category.html",
            {
                "products": products,
                "category": category,
                "categories": Category.objects.all,
            },
        )

    except:
        messages.success(request, ("카테고리가 존재하지 않습니다."))
        return redirect("store:home")


def category_summary(request):
    categories = Category.objects.all()
    return render(request, "store/category_summary.html", {"categories": categories})


def search(request):
    # Determin if they filled out the form
    if request.method == "POST":
        searched = request.POST["searched"]

        searched = Product.objects.filter(
            Q(name__icontains=searched) | Q(description__icontains=searched)
        )
        print("서치=======", searched)

        # Test for null
        if not searched:
            messages.success(request, "해당 상품이 없습니다....")
            return render(request, "store/search.html", {})
        else:
            return render(request, "store/search.html", {"searched": searched})
    else:
        return render(request, "store/search.html", {})
