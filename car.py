from check_service import CheckService


class Car(CheckService):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    def service_needed(self):
        return self.battery.service_needed() or self.engine.service_needed()
