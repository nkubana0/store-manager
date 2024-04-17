import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #assert statements 
        assert price >= 0, f"Price : {price} is not equal or greater than zero!"
        assert quantity >= 0, f"Quantity : {quantity} is not equal or greater than zero!"
        
        #assign self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        #append items to all
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instatiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'), 
                price= float(item.get('price')),
                quantity= float(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"
