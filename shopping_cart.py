import math

class ShoppingCart:
    def __init__(self, employee_discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount
        self._median_list = []
        self._items_dict = {}

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self,total):
        self._total = total

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def employee_discount(self):
        return self._employee_discount

    @employee_discount.setter
    def employee_discount(self, employee_discount):
        self._employee_discount = employee_discount

    # @property
    # def median_list(self):
    #     return self._median_list
    #
    # @median_list.setter
    # def median_list(self, median_list):
    #     self._median_list = median_list

    def add_item(self, name, price, quantity=1):
        added_cost = price * quantity
        self._total += added_cost
        num = 0
        while num < quantity:
            self._items_dict  = {'name': name, 'price': price}
            self._items.append(self._items_dict)
            self._median_list.append(price)
            num +=1
        return self._total

    def mean_item_price(self):
        return self._total/len(self._items)

    def median_item_price(self):
        sorted_list = sorted(self._median_list)
        middle = int((len(sorted_list)) / 2)
        if len(sorted_list)%2 != 0:
            return sorted_list[middle]
        else:
            return (sorted_list[middle] + sorted_list[middle-1])/2

    def apply_discount(self):
        if self._employee_discount == None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            return self._total * ((100 - self._employee_discount)/100)

    def item_names(self):
        return [dict['name'] for dict in self._items]

    def void_last_item(self):
        if len(self._items) == 0:
            return "There are no items in your cart!"
        else:
            removed_item = self._items.pop()
            self._total -= removed_item['price']
            return self._total
