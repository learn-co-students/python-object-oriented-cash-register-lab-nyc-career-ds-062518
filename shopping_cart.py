from numpy import median

class ShoppingCart:

    price_list = {}

    def __init__(self, employee_discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, newtotal):
        self._total = newtotal

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, newitems):
        self._items = newitems

    @property
    def employee_discount(self):
        return self._employee_discount

    @employee_discount.setter
    def employee_discount(self, newemployee_discount):
        self._employee_discount = newemployee_discount

    def add_item(self, itemname, itemprice, quantity = 1):
        self.price_list.update({itemname: itemprice})
        for i in range(quantity):
            self._items.append({'name': itemname, 'price': itemprice})
        self._total += quantity * itemprice
        return self._total

    def mean_item_price(self):
        return self._total / len(self._items)

    def median_item_price(self):
        prices = []
        for item in self._items:
            price = item['price']
            prices.append(price)
        return median(prices)

    def apply_discount(self):
        if self._employee_discount != None:
            return self.total * (1 - self._employee_discount / 100)
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def item_names(self):
        list = []
        for item in self._items:
            list.append(item['name'])
        return list

    def void_last_item(self):
        if len(self._items) > 0:
            self._total -= self._items[-1]['price']
            self._items.pop()
        else:
            return "There are no items in your cart!"
