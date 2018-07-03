class ShoppingCart:

    def __init__(self, employee_discount = None):
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
    def items(self, items):
        self._items = items

    @property
    def employee_discount(self):
        return self._employee_discount

    @employee_discount.setter
    def employee_discount(self, employee_discount):
        self._employee_discount = employee_discount

    def add_item(self, name, price, quantity = 1):
        item_dict = {'name' : name, 'price' : price}
        self._total += price*quantity
        for i in range(quantity):
            self._items.append(item_dict)
        return self._total

    def mean_item_price(self):
        mean = self._total/len(self._items)
        return mean

    def median_item_price(self):
        price_list = [item['price'] for item in self._items]
        price_list.sort()
        if len(self._items)%2: # if we know we have an odd amount
            return price_list[int((len(price_list)+1)/2-1)]
        else: # for even
            upper_median = price_list[int((len(price_list)/2))-1]
            lower_median = price_list[int((len(price_list)/2))]
            return (upper_median + lower_median)/2
#            return ((price_list[int((len(price_list)/2))]+price_list[int((len(price_list)/2)+1)])/2)

    def apply_discount(self):
        if not self._employee_discount:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            return self._total*(1- self._employee_discount/100)

    def item_names(self):
        item_list = [item['name'] for item in self._items]
        return item_list

    def void_last_item(self):
        if not self._items:
            return("There are no items in your cart!")
        else:
            voided = self.items.pop()
            self._total -= voided['price']
        return self.items
