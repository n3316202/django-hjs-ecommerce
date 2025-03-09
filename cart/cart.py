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
