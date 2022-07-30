import unittest
from datetime import date
from battery.nubbin import Nubbin
from battery.spindler import Spindler
from engine.capulet import Capulet
from engine.sternman import Sternman
from engine.willoughby import Willoughby
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime


class TestNubbin(unittest.TestCase):
    def test_service_not_needed(self):
        curr_service_date = date.fromisoformat("2022-07-29")
        prev_service_date = date.fromisoformat("2022-07-07")
        nubbin_battery = Nubbin(curr_service_date, prev_service_date)
        self.assertFalse(nubbin_battery.service_needed())

    def test_service_needed(self):
        curr_service_date = date.fromisoformat("2022-07-29")
        prev_service_date = date.fromisoformat("2018-07-07")
        nubbin_battery = Nubbin(curr_service_date, prev_service_date)
        self.assertTrue(nubbin_battery.service_needed())


class TestSpindler(unittest.TestCase):
    def test_service_not_needed(self):
        curr_service_date = date.fromisoformat("2022-07-29")
        prev_service_date = date.fromisoformat("2022-07-07")
        spindler_battery = Spindler(curr_service_date, prev_service_date)
        self.assertFalse(spindler_battery.service_needed())

    def test_service_needed(self):
        curr_service_date = date.fromisoformat("2022-07-29")
        prev_service_date = date.fromisoformat("2019-07-07")
        spindler_battery = Spindler(curr_service_date, prev_service_date)
        self.assertTrue(spindler_battery.service_needed())


class TestCapulet(unittest.TestCase):
    def test_service_not_needed(self):
        net_mileage = 30000
        capulet_engine = Capulet(net_mileage, 0)
        self.assertFalse(capulet_engine.service_needed())

    def test_service_needed(self):
        net_mileage = 30001
        capulet_engine = Capulet(net_mileage, 0)
        self.assertTrue(capulet_engine.service_needed())


class TestSternman(unittest.TestCase):
    def test_service_not_needed(self):
        has_warning = False
        sternman_engine = Sternman(has_warning)
        self.assertFalse(sternman_engine.service_needed())

    def test_service_needed(self):
        has_warning = True
        sternman_engine = Sternman(has_warning)
        self.assertTrue(sternman_engine.service_needed())


class TestWilloughby(unittest.TestCase):
    def test_service_not_needed(self):
        net_mileage = 60000
        willoughby_engine = Willoughby(net_mileage, 0)
        self.assertFalse(willoughby_engine.service_needed())

    def test_service_needed(self):
        net_mileage = 60001
        willoughby_engine = Willoughby(net_mileage, 0)
        self.assertTrue(willoughby_engine.service_needed())


class TestCarrigan(unittest.TestCase):
    def test_service_not_needed(self):
        tire_wear = [0, 0, 0, 0]
        carrigan_tires = Carrigan(tire_wear)
        self.assertFalse(carrigan_tires.service_needed())

    def test_service_needed(self):
        tire_wear = [0, 0, 0, 0.9]
        carrigan_tires = Carrigan(tire_wear)
        self.assertTrue(carrigan_tires.service_needed())


class TestOctoprime(unittest.TestCase):
    def test_service_not_needed(self):
        tire_wear = [0, 0, 0, 0]
        octoprime_tires = Octoprime(tire_wear)
        self.assertFalse(octoprime_tires.service_needed())

    def test_service_needed(self):
        tire_wear = [0.9, 0.8, 0.7, 0.7]
        octoprime_tires = Octoprime(tire_wear)
        self.assertTrue(octoprime_tires.service_needed())
