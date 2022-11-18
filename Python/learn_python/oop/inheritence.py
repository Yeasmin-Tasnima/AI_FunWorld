class Vehicle:
    def general_usage(self):
        print('General usage: Transportation.')


class Car(Vehicle):
    def __init__(self):
        self.wheel = 4
        self.has_roof = True
        print('I am Car.')

    def specific_usage(self):
        self.general_usage()
        print('Specific usage: Family Vacation.')


class MotorCycle(Vehicle):
    def __init__(self):
        self.wheel = 2
        self.has_roof = False
        print('I am Motorcycle.')

    def specific_usage(self):
        self.general_usage()
        print('Specific usage: Racing.')


c = Car()
c.specific_usage()

m = MotorCycle()
m.specific_usage()

print(isinstance(c, Car))
print(issubclass(Car, Vehicle))
