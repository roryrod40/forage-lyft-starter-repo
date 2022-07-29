from battery.battery import Battery, add_years


class Nubbin(Battery):
    def __init__(self, curr_service_date, prev_service_date):
        self.curr_service_date = curr_service_date
        self.prev_service_date = prev_service_date

    def service_needed(self):
        return add_years(self.prev_service_date, 4) < self.curr_service_date
