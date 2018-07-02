class ShoppingCart:

    def __init__(self, employee_discount=None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, list_of_items):
        self._items = list_of_items

    @property
    def employee_discount(self):
        return self._employee_discount

    @employee_discount.setter
    def employee_discount(self, discount):
        self._employee_discount = discount


    # methods
    def add_item(self, name, price, quantity=1):
        for item in list(range(quantity)):
            self._items.append({'name': name, 'price': price})
            self._total += price
        return self._total

    def mean_item_price(self):
        return self._total/len(self._items)

    def median_item_price(self):
        prices = [item['price'] for item in self._items]
        prices.sort()
        return self.find_median(prices)

    def find_median(self, sorted_items):
        length = len(sorted_items)
        if length %2 == 0:
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (sorted_items[mid_one] + sorted_items[mid_two])/2
            return median
        mid = int(length/2)
        return sorted_items[mid]

    def apply_discount(self):
        if self.employee_discount:
            disc_multiplier = (1- self.employee_discount/100)
            disc_total = disc_multiplier*self.total
            return disc_total
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def item_names(self):
        return [item['name'] for item in self.items]

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']
