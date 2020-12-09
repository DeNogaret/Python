from vehicle import Vehicle


class Boat(Vehicle):
    def __init__(self, fuel_tank, engine, wheels):
        super(Boat, self).__init__(fuel_tank, engine, wheels)

    def acceleration(self):
        print('The speed of the boat:  ' + str(self.speed))
        super(Boat, self).acceleration()

    def turn(self, side):
        print('The boat turned')
        super(Boat, self).turn(side)

    def brake(self):
        super(Boat, self).brake()
        print('The boat stopped')

    def get_wheels_number(self):
        super(Boat, self).get_wheels_number()
