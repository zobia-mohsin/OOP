import CarClass as c

#car = float(input("Enter the year and make of your car: "))
#car = c.Car(1990, 'Honda')
year_model = float(input("What is the model year of the car? "))
make = input("What is the make of the car? ")

car = c.Car(year_model, make)

#print = ("We are referring to this car", car, '.')

print("The car is accelerating at: ")
for i in range(5):
    car.set_accelerate()
    speed = car.get_speed()
    print(car.get_speed())


print("The car is deaccelerating at: ")
for i in range(5):
    car.set_brake()
    speed = car.get_speed()
    print(car.get_speed())
