import random

class Insect:
    
    def __init__(self):
        self.legs = '4'
        self.wings = '2'
        self.flight_distance = '0'
    

    def calc_flight(self):
        self.flight_distance = random.randint(1,10)

    def get_miles(self):
        return self.flight_distance


