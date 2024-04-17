from item import Item


class Phone (Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #call super
        super().__init__(
            name, price, quantity
        )
        #assert statements 
        assert broken_phones >= 0, f"Broken Phones : {broken_phones} is not equal or greater than zero!"

        #assign self objects
        self.broken_phones = broken_phones

        #append items to all
        Phone.all.append(self)