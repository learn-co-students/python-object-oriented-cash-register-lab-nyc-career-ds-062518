class ShoppingCart:

    def __init__(self):
        self._total = 0
        self._items = []
        self._employee_discount = None

    #decorators for _total

        @property
        def total(self):
            return self._total

        @total.setter
        def total(self, total):
            self._total = total

    #decorators for _items
        @property
        def items(self):
            return self._items

        @items.setter
        def items(self, *items):
            for item in items:
                self._items.append(item)
        #note that this should allow adding multiple items, but not with price, for that,
        #you should use add_items

    #decorators for _employee_discount
        @property
        def employee_discount(self):
            return self._employee_discount

        @employee_discount.setter
        def employee_discount(self, employee_discount):
            self._employee_discount = employee_discount

        def add_item(self, name, price, quantity = 1):
            for i in range(quantity):
                self._items.append({"name" : name, "price" : price})
            self._total += price*quanitity
            return self._total
