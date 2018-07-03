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

    def add_item (self, name, price, quantity = 1):
        #self._name = name
        self._total += price * quantity
        for q in list(range(quantity)):
            self._items.append({'name':name, 'price':price})
        #print(self._items)
        return self._total

    def mean_item_price(self):
        return ((self._total)/ len(self._items))

    def median_item_price(self):
        med_items = []
        for item in self._items:
            med_items.append(item['price'])
        sort_items = sorted(med_items)
        if len(sort_items)%2 ==0:
            num =int(len(sort_items)/2)
            return ((sort_items[num-1]+ sort_items[num])/2)
        else:
            num =int(((len(sort_items) +1)/2))
            return (sort_items[num-1])

    def apply_discount(self):
        if self._employee_discount is  None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            return (1 - (self._employee_discount/100) )*(self._total)

    def item_names(self):
        items_names_list = []
        for item in self._items:
            items_names_list.append(item['name'])
        return items_names_list

    def void_last_item(self):
        if self._items==[]:
            return "There are no items in your cart!"
        else:
            self._total-= self._items[-1]['price']
            self._items.pop()
            #    return self._items
            return self._total
