from django.db import models

# Create your models here.
from django.db import models


# dev_22
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"카트아이디:{self.id}    유저이름:{self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_items"
    )  # related_name 역참조
    product = models.ForeignKey(
        "store.Product", on_delete=models.CASCADE, related_name="items"
    )
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"자기아이디:{self.id}    카트아이디:{self.cart.id}   제품아이디:{self.product.id}   제품이름:{self.product.name}   제품수량:{self.quantity}"
