from boat import Boat
from car import Car
from engine import Engine
from fuel_tank import FuelTank
from solar_car import SolarCar
from wheels import Wheels


def drive(driveable):
    driveable.get_wheels_number()
    driveable.turn('right')
    driveable.acceleration()
    driveable.turn('left')
    driveable.brake()


if __name__ == '__main__':
    car = Car(FuelTank(114), Engine(120), Wheels(4))
    solarCar = SolarCar(FuelTank(80), Engine(120), Wheels(6))
    boat = Boat(FuelTank(88), Engine(50), Wheels(0))

    for i in [boat, car, solarCar]:
        drive(i)
