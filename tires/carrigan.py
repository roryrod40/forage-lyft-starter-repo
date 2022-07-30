from tires.tires import Tires


class Carrigan(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def service_needed(self):
        service_needed = False
        for tire in self.tire_wear:
            if tire >= 0.9:
                service_needed = True
        return service_needed
