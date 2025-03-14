from sre_constants import POSSESSIVE_REPEAT
from django.shortcuts import get_object_or_404, render

from orders.models import Order


# Create your views here.
def payment_process(request):
    order_id = request.session.get("order_id", None)
    print(order_id)
    order = get_object_or_404(Order, id=order_id)
    print(order.values())

    if request.method == "POST":
        pass
    else:
        return render(request, "payment/process.html".order.values())
