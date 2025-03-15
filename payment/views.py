from sre_constants import POSSESSIVE_REPEAT
from django.shortcuts import get_object_or_404, render

from cart.cart import Cart
from orders.forms import ShippingForm
from orders.models import Order, ShippingAddress
from django.contrib.auth.decorators import login_required

from payment.models import Payment


# dev_25
# Create your views here.
@login_required
def payment_process(request):

    # 결제 성공 시 로직
    # 1.주문 정보 저장을 위해 ajax 요청
    # 2.서버에서 결재금액과 주문금액(세션에 저장되어있는)이 일치하는지 확인
    # 3.일치하면 주문 정보 및 결재정보 저장
    if request.POST:

        cart = Cart(request)
        df_order = cart.get_data_frame_products()
        # DataFrame을 딕셔너리 리스트로 변환
        dic_orders = df_order.to_dict(orient="records")
        total_price = cart.cart_total()

        # if total_price == int(request.POST['paid_amount']): #테스트를 위하여 10으로 넣고 대입입
        if 100 == int(request.POST["paid_amount"]):
            # logged in
            user = request.user

            # create order
            create_order = Order(user=user)
            create_order.amount_paid = total_price
            create_order.save()

            #OrderItem를 저장 
            order_id = create_order.pk
            
            
            
            
            
            #결재 데이터 저장
            create_payment = Payment(order=create_order)
            create_payment.imp_uid = request.POST['imp_uid']
            create_payment.save()
            
            
        # Get Current uer's shipping Info
        # shipping_user = ShippingAddress.objects.get(id=request.user.id)
        # print(shipping_user)
        # Get User's Shipping Form
        # form = ShippingForm(instance=shipping_user)
        # form = ShippingForm(request.POST or None, instance=shipping_user)

        # if form.is_valid():
        #     form.save()
        #     #Save shipping form
        #     form.save()

    # order_id = request.session.get("order_id", None)
    # print(order_id)
    # order = get_object_or_404(Order, id=order_id)
    # print(order)

    # if request.method == "POST":
    #     pass
    # else:
    #     return render(request, "payment/process.html", {"order": order})
