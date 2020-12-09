from car import Car


class SolarCar(Car):
    def __init__(self, fuel_tank, engine, wheels):
        super(SolarCar, self).__init__(fuel_tank, engine, wheels)

    def acceleration(self):
        print('The speed of solar car: ' + str(self.speed))
        super(SolarCar, self).acceleration()

    def turn(self, side):
        print('The solar car turned')
        super(SolarCar, self).turn(side)

    def brake(self):
        super(SolarCar, self).brake()
        print('The solar car stopped')

    def get_wheels_number(self):
        super(SolarCar, self).get_wheels_number()
