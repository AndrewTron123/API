

class CellPhoneClass:
    def __init__(self, manufact, model, retail_price):
        self.manufact = manufact
        self.model = model
        self.retail_price = retail_price


    def set_manufact(self, manufact):
        self.manufact = manufact

    def set_model(self, model):
        self.model = model

    def set_retail_price(self, retail_price):
        self.manufact = retail_price 
    
    def get_manufact(self):
        return self.manufact
    
    def get_model(self):
        return self.model
    
    def get_retail_price(self):
        return self.retail_price
    
    def display(self):
        manufact = self.get_manufact()
        model = self.get_model()
        price = self.get_retail_price()

        print(f' The manufactur is {manufact}, the model is {model}, the price is {price}')

        

    
    