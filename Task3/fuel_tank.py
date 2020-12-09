class FuelTank(object):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self):
        return round(self.capacity * 1.7)
