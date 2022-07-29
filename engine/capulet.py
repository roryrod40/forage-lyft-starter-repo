from engine.engine import Engine


class Capulet(Engine):
    def __init__(self, curr_mileage, prev_mileage):
        self.curr_mileage = curr_mileage
        self.prev_mileage = prev_mileage

    def service_needed(self):
        return self.curr_mileage - self.prev_mileage > 30000
