from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

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

        return thing

    # dev_18
    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.save()

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
