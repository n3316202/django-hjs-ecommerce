from django.contrib import admin

from orders.models import Order, OrderItem, ShippingAddress

# Register your models here.
# dev_23
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
