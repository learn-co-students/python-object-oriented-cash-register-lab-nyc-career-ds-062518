class ShoppingCart:
    def __init__(self, _employee_discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = _employee_discount
        self._median_list = []
        self._item_dict = {}

    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, _total):
        self._total = _total

    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, _items):
        self._items = _items

    @property
    def employee_discount(self):
        return self._employee_discount
    @employee_discount.setter
    def employee_discount(self, _employee_discount):
        self._employee_discount = _employee_discount

    def add_item(self, name, price, quantity = 1):
        item_cost = price * quantity
        self._total += item_cost
        c = 0
        while c < quantity:
            self._item_dict = {'name' :name, 'price':price}
            self._items.append(self._item_dict)
            self._median_list.append(price)
            c+=1
        return self._total

    def mean_item_price(self):
        return self._total / len(self._items)
    def median_item_price(self):
        sorted_list = sorted(self._median_list)
        if len(sorted_list) % 2 != 0:
            return sorted_list[int(len(sorted_list)/2)]
        else:
            a = int(len(sorted_list)/2)
            b = int(a - 1)
            return (sorted_list[a] + sorted_list[b])/2

    def apply_discount(self):
        if self._employee_discount == None:
            return 'Sorry, there is no discount to apply to your cart :('
        return self._total * (100-self._employee_discount) / 100

    def item_names(self):
        return [dict['name'] for dict in self._items]

    def void_last_item(self):
        if len(self._items) == 0:
            return 'There are no items in your cart!'
        else:
            last_item = self._items.pop()
            self._total -= last_item['price']
            return self._total
