import CarClass as c

car = c.CarClass('2015','Ford')

for i in range(5):
    car.calculate_acceleration()
    print(f"Current speed: {car.get_speed()} mph")

for i in range(5):
    car.calculate_brake()
    print(f"Current speed: {car.get_speed()} mph")

