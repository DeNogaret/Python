from abc import ABC


class Driveable(ABC):

    def acceleration(self):
        pass

    def turn(self, side):
        pass

    def brake(self):
        pass
