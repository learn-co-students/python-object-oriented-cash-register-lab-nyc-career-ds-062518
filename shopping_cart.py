class ShoppingCart:

    def __init__(self, employee_discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount

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
    def items(self, items):
        if not self._items:
            self._items = items

    #did for the test, but it appears to be wrong. Should either throw error at
    #user telling them to use add_items method or should only take input of dict.
    #could inform user of this also. Current method *only* works in limited circumstance
    #i.e., if items is intialized with a list using this setter call. Change init value
    #back to = [] from None once fixed

#decorators for _employee_discount
    @property
    def employee_discount(self):
        return self._employee_discount

    @employee_discount.setter
    def employee_discount(self, employee_discount):
        self._employee_discount = employee_discount

### INSTANCE METHODS ###

    def add_item(self, name, price, quantity = 1):
        for i in range(quantity):
            self._items.append({"name" : name, "price" : price})
        self._total += price*quantity
        return self._total

    def mean_item_price(self):
        mean_price = self._total/len(self._items)
        return mean_price

    def median_item_price(self):
        price_list = [item['price'] for item in self._items]
        price_list.sort()
        print(price_list, len(price_list))
        if len(self._items)%2: # if we know we have an odd amount
            return price_list[int((len(price_list)-1)/2)]
        else: #if we know we have an even
            upper_median = price_list[int((len(price_list)/2)-1)]
            lower_median = price_list[int(len(price_list)/2)]
            return (upper_median + lower_median)/2



    def apply_discount(self):
        if self._employee_discount is None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            return self._total * (1 - self._employee_discount/100)

    def item_names(self):
        item_names = [item['name'] for item in self._items]
        return item_names

    def void_last_item(self):
        if not self._items:
            return "There are no items in your cart!"
        else:
            voided = self._items.pop()
            self._total -= voided['price']
        return self._items
        return self._total
    #you could probably build this with some sort of *args and *kwargs methodology
    #to add multiple items in a single instance
