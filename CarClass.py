class Car:

    def __init__(self, year_model, make):
        self.__year_model_of_car = year_model
        self.__make = make
        self.__speed = 0

    def set_accelerate(self):
        self.__speed += 5

    def set_brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
