class ShoppingCart:

    def __init__(self, employee_discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount

    def mean_item_price_list(self):
        price_list = []
        for item in self._items:
            price_list.append(item['price'])
        return price_list

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
        self._total += price * quantity
        num = 1
        while num <= quantity:
            self._item_dict = {'name': name, 'price': price}
            self._items.append(self._item_dict)
            num += 1
        return self._total

    def mean_item_price(self):
        mean_item_price_list = self.mean_item_price_list()
        mean_price = sum(mean_item_price_list)/len(mean_item_price_list)
        return mean_price

    def median_item_price(self):
        price_list = self.mean_item_price_list()
        median_price_list = sorted(price_list)
        list_length = len(median_price_list)
        if list_length % 2 != 0:
            median_price = median_price_list[(list_length // 2 )]
            return median_price
        else:
            lower_median = median_price_list[int((list_length//2) - 1)]
            upper_median = median_price_list[int(list_length//2)]
            median_price = (lower_median + upper_median) / 2
            return median_price

    def apply_discount(self):
        discount = self._employee_discount
        if discount == None:
            return 'Sorry, there is no discount to apply to your cart :('
        else:
            return self._total * (1 - (discount/100))

    def item_names(self):
        item_list = []
        for item in self._items:
            item_list.append(item['name'])
        return item_list

    def void_last_item(self):
        items = self._items
        if items == []:
            return 'There are no items in your cart!'
        else:
            popped_item = items.pop()
            self._total -= popped_item['price']
            return self._total
