from tires.tires import Tires


class Octoprime(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def service_needed(self):
        total_wear = 0
        for tire in self.tire_wear:
            total_wear += tire
        return total_wear >= 3
