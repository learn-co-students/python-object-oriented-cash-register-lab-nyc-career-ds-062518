class ShoppingCart:

    def __init__(self, employee_discount = None,  total = 0):
        self._total = total
        self._items = []
#        self._item_names = []
#        self._item_price = []
        self._employee_discount = employee_discount

    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, total):
        self._total = total

#       Path/ learn -- returns the following
#   [Previous line repeated 1466 more times]
# RecursionError: maximum recursion depth exceeded while calling a Python object
# What is happening here exaactly? Recursion error?

    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, item_insert):
        self._items = self._items + item_insert


    @property
    def employee_discount(self):
        return self._employee_discount
    @employee_discount.setter
    def employee_discount(self, employee_discount):
        self._employee_discount = employee_discount

    def add_item(self, item, price, num_items = 1):
        for i in range(0,num_items):
            self._items.append({'name': item, 'price': price})
        self.total += (num_items)*price
        return self.total

    @property
    def item_price(self):
        return [self.items[i]['price'] for i in range(0, len(self.items))]

    def item_names(self):
        return [self.items[i]['name'] for i in range(0, len(self.items))]

    def mean_item_price(self):
        return self.total / len(self.items)

    def median_item_price(self):
        sorted_item_price = sorted(self.item_price, key=int)
        len_sorted_item_price = len(sorted_item_price)/2
        if len(sorted_item_price)%2 == 0:
            a = sorted_item_price[int(len_sorted_item_price)-1]
            b = sorted_item_price[int(len_sorted_item_price)]
            return (a+b)/2
        else:
            return sorted(sorted_item_price)[int(len(sorted_item_price)/2)]

    def apply_discount(self):
        if self.employee_discount == None:
            return 'Sorry, there is no discount to apply to your cart :('
        else:
            return self.total*(1-(self.employee_discount/100))

    def void_last_item(self):
        if len(self.items) == 0:
            return "There are no items in your cart!"
        else:
            self.total -= self.item_price[-1]
            del self.items[-1]
