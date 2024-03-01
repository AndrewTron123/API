class CarClass:
    def __init__(self,year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def calculate_acceleration(self):
        self.__speed += 5
    
    def calculate_brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return(self.__speed)

    





