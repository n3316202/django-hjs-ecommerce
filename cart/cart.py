from cart.models import CartItem
from store.models import Product
from store.models import Product
from cart.models import Cart as CartModel


class Cart:
    def __init__(self, request):
        self.session = request.session

        # dev_22
        # Get request
        self.request = request

        # Get the current session key if it exists
        cart = self.session.get("session_key")

        # If the session key does not exist, create one!
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        print(cart)

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product, quantity):

        product_id = str(product.id)
        product_qty = str(quantity)

        # >>> a[3] = [1, 2, 3]
        # >>> a
        # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.save()

    def __len__(self):
        return len(self.cart)

    def save(self):
        self.session.modified = True  # 세션 저장

    # dev_16 함수 이름및 수정
    def get_products(self):

        # Get ids from cart
        product_ids = self.cart.keys()

        # use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)

        # Return those looked up products
        return products

    def get_quantities(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # Get cart
        ourcart = self.cart
        # {'4':3, '5':4}}

        # update dictionary
        ourcart[product_id] = product_qty

        self.save()
        thing = self.cart

        # dev_22
        if self.request.user.is_authenticated:

            # Get the current user profile
            cart, created = CartModel.objects.get_or_create(user=self.request.user)
            print(cart)
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product_id=product_id
            )
            cart_item.quantity = quantity
            print(cart_item)
            cart_item.save()

        return thing

    # dev_18
    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.save()

        # dev_40
        # Deal with logged in user
        if self.request.user.is_authenticated:

            # Get the current user profile
            cart, created = CartModel.objects.get_or_create(user=self.request.user)
            print(cart)
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product_id=product_id
            )
            print(cart_item)
            cart_item.delete()

    # dev_19
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        quantities = self.cart

        total = 0

        for key, value in quantities.items():
            # Convert key string into so we
            key = int(key)

            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)

        return total

    # https://www.youtube.com/watch?v=PgCMKeT2JyY
    # dev_22
    def add_to_cart(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        # self.session.modified = True
        self.save()

        # product = Product.objects.get(id=product_id)

        # Deal with logged in user
        if self.request.user.is_authenticated:

            # Get the current user profile
            cart, created = CartModel.objects.get_or_create(user=self.request.user)
            print(cart)
            # Object: The existing object that was found with the given kwargs
            # Boolean: Specifies whether a new object was created
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product=product
            )
            print(cart_item)
            cart_item.quantity = int(quantity)
            cart_item.save()
