class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item("Phone", 100, 5)

item2 = Item("Laptop",1000, 3)

print(item1.quantity)
print(item2.quantity)