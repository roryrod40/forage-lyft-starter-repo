from car import Car
from battery.nubbin import Nubbin
from battery.spindler import Spindler
from engine.capulet import Capulet
from engine.sternman import Sternman
from engine.willoughby import Willoughby
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime


class CarFactory:
    @staticmethod
    def create_calliope(current_service_date, prev_service_date, curr_mileage, prev_mileage, tire_wear):
        battery = Spindler(current_service_date, prev_service_date)
        engine = Capulet(curr_mileage, prev_mileage)
        tires = Carrigan(tire_wear)
        car = Car(battery, engine, tires)
        return car

    @staticmethod
    def create_glissade(current_service_date, prev_service_date, curr_mileage, prev_mileage, tire_wear):
        battery = Spindler(current_service_date, prev_service_date)
        engine = Willoughby(curr_mileage, prev_mileage)
        tires = Carrigan(tire_wear)
        car = Car(battery, engine, tires)
        return car

    @staticmethod
    def create_palindrome(current_service_date, prev_service_date, has_warning, tire_wear):
        battery = Spindler(current_service_date, prev_service_date)
        engine = Sternman(has_warning)
        tires = Carrigan(tire_wear)
        car = Car(battery, engine, tires)
        return car

    @staticmethod
    def create_rorschach(current_service_date, prev_service_date, curr_mileage, prev_mileage, tire_wear):
        battery = Nubbin(current_service_date, prev_service_date)
        engine = Willoughby(curr_mileage, prev_mileage)
        tires = Octoprime(tire_wear)
        car = Car(battery, engine, tires)
        return car

    @staticmethod
    def create_thovex(current_service_date, prev_service_date, curr_mileage, prev_mileage, tire_wear):
        battery = Nubbin(current_service_date, prev_service_date)
        engine = Capulet(curr_mileage, prev_mileage)
        tires = Octoprime(tire_wear)
        car = Car(battery, engine, tires)
        return car
