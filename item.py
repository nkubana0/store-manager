import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #assert statements 
        assert price >= 0, f"Price : {price} is not equal or greater than zero!"
        assert quantity >= 0, f"Quantity : {quantity} is not equal or greater than zero!"
        
        #assign self objects
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #append items to all
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
        
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
        
    @property
    def name(self):
        return self.name
        
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long')
        else:
            self.__name = value
    
    def calculate_total_price(self):
        return self.__price * self.quantity

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
        return f"Item ('{self.name}', {self.__price}, {self.quantity})"
    
    def connect(self, smpt_server):
        pass

    def prepare_body(self):
        return f"""
        Hello Sir/Madam.
        We have {self.name} {self.quantity} times.
        Regards, Shema Ivan
        """
    def send_email(self):
        pass