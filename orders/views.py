from django.shortcuts import redirect, render

from cart.cart import Cart
from django.contrib import messages

from orders.forms import ShippingForm
from .models import Order, OrderItem, ShippingAddress

import pandas as pd
from cart.models import Cart as CartModel, CartItem


# dev_24
# Create your views here.
def orders_create(request):

    if request.POST:

        cart = Cart(request)
        # cart_products = cart.get_products
        # quantiles = cart.get_quantities
        # cart_delete = cart.delete

        # totals = cart.cart_total()
        # print(totals)

        if request.user.is_authenticated:

            # logged in
            user = request.user

            # 카트 데이타 프레임 가져오기
            df_cart = cart.get_data_frame_products()

            # Create Order
            create_order = Order(user=user)
            create_order.amount_paid = df_cart["sum_price"].sum()
            create_order.save()

            # Add Order Items
            # Get the oorder ID
            order_id = create_order.pk

            for index, row in df_cart.iterrows():
                # Create Order Item
                create_order_item = OrderItem(
                    order_id=order_id,
                    product_id=row["id"],
                    quantity=row["quantity"],
                    price=row["final_price"],
                )
                create_order_item.save()

            for key in list(cart.cart.keys()):
                cart.delete(key)

            # 배송지 업데이트
            # Get Current uer's shipping Info
            # shipping_user = ShippingAddress.objects.get(id=request.user.id)

            # Get User's Shipping Form
            form = ShippingForm(request.POST)

            if form.is_valid():
                shipping = form.save(commit=False)  # 저장은 하지 않고 객체만 생성
                shipping.user = (
                    request.user
                )  # ForeignKey 값 추가 (현재 로그인한 사용자)
                shipping.save()  # 최종적으로 저장

            # dev_24
            messages.success(request, "주문이 완료 되었습니다.")
            request.session["order_id"] = order_id
            return redirect("payment:process")  # 주문 완료후 결제 프로세스로 이동

        else:
            messages.success(request, "You Must be logged In To order the products")
            return redirect("/login")

    else:

        cart = Cart(request)
        df_order = cart.get_data_frame_products()
        # DataFrame을 딕셔너리 리스트로 변환
        dic_orders = df_order.to_dict(orient="records")
        total_price = cart.cart_total()

        # Get Current uer's shipping Info
        shipping_user = ShippingAddress.objects.get(id=request.user.id)

        # Get User's Shipping Form
        form = ShippingForm(request.POST or None, instance=shipping_user)

        return render(
            request,
            "orders/create.html",
            {"dic_orders": dic_orders, "total_price": total_price, "form": form},
        )
