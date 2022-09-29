import datetime

class Prices():

    def __init__(self):
        self.coffee = 2.50
        self.flat_wite = 3.25
        self.cappucino = 3.00
        self.moccacino = 3.50
        self.items_machine = {'Coffee':self.coffee, 'Flat White': self.flat_wite, 'Cappucino': self.cappucino, 'Moccacino': self.moccacino}
        self.cash = 0
        self.items_bought = {key: 0 for key, _ in self.items_machine.items()}
        self.date = datetime.datetime.today()

    
    def add_to_bought(self, key):
        self.items_bought[key] += 1
        print(self.items_bought)
        self.add_cash(key)

    def add_cash(self, key):
        price_product = self.items_machine[key]
        self.cash += price_product
        print(self.cash)



    