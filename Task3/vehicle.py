from driveable import Driveable


class Vehicle(Driveable):

    def __init__(self, fuel_tank, engine, wheels):
        self.fuel_tank = fuel_tank
        self.engine = engine
        self.wheels = wheels.get_number()
        self.speed = 0

    def get_wheels_number(self):
        if self.wheels == 0:
            print("This vehicle has no wheels")
        else:
            print('The number of wheels: ' + str(self.wheels))

    def acceleration(self):
        self.speed = self.speed + self.fuel_tank.get()
        print('Acceleration to:  ' + str(self.speed) + 'km/h')

    def turn(self, side):
        print('Turn ' + str(side))

    def brake(self):
        while self.speed != 0:
            self.speed = self.speed - (self.speed / 2)
            if self.speed == 1:
                self.speed = 0
                break
            print('The speed now is: ' + str(self.speed) + 'km/h')
            break
        print('Stop')
