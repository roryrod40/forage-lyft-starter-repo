from abc import ABC


class Battery(ABC):
    def service_needed(self):
        pass


def add_years(prev_service_date, years):
    return prev_service_date.replace(year=prev_service_date.year + years)
