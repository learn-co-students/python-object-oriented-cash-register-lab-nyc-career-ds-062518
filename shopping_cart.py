import math
class ShoppingCart:

    def __init__(self, employee_discount = None):
        #when get to discount pay attention about the defaults
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
        self._total += round(price * quantity,2)
        for q in list(range(quantity)):
            self._items.append({'name' : name, 'price': price}) #: "$" + str(round(price, 2))})
        print(self._items)
        return self._total

    def mean_item_price(self):
        return (self._total/len(self._items))

    def median_item_price(self):
        med_items = []
        for item in self._items:
            med_items.append(item['price'])
        order = sorted(med_items)
        if len(med_items)%2 == 0:
            #print(order)
            num = int(len(med_items)/2)
            return ((order[num-1] + order[num])/2)
#            return order[num-1]
        else:
            num = int((len(med_items) +1)/2)
            return order[num-1]

    def apply_discount(self):
            if self._employee_discount == None:
                return "Sorry, there is no discount to apply to your cart :("
            else:
                return self._total * (1 - (self._employee_discount/ 100))

    def item_names(self):
        return list(map(lambda x: x['name'], self._items))
        #return items#(item for item in self._items[item]['name'])

    def void_last_item(self):
        if self._items == []:
            return "There are no items in your cart!"
        else:
            self._total -= self._items[-1]['price']
            self._items.pop()
            return self._total
