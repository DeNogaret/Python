from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, fuel_tank, engine, wheels):
        super(Car, self).__init__(fuel_tank, engine, wheels)

    def acceleration(self):
        print('The speed of the car:  ' + str(self.speed))
        super(Car, self).acceleration()

    def turn(self, side):
        print('The car turned')
        super(Car, self).turn(side)

    def brake(self):
        super(Car, self).brake()
        print('The car stopped')

    def get_wheels_number(self):
        super(Car, self).get_wheels_number()
