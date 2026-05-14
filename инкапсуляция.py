class Order:
    def __init__(self):
        self._products = []
        self.__total_price = 0

    def add_product(self, product):
        self._products.append(product)
        self.__recalc(product)

    def __recalc(self, product):
        self.__total_price += product['price']

    def get_total_price(self):
        return self.__total_price

order = Order()
print(order.get_total_price())


product = {'name': 'bread', 'price': 10}
product1 = {'name': 'coffee', 'price': 210}

order.add_product(product)
order.add_product(product1)

print(order.__dict__)
