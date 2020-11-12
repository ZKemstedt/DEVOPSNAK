import unittest
from lesson_4.car import Car


class CarTest(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_create_car_empty(self):
        self.assertIsInstance(self.car, Car)

    def test_horn_loud(self):
        self.assertEqual(self.car.horn(), "loud sound")

    def test_started_default(self):
        car = Car()
        self.assertEqual(car.started, False)

    def test_start_started_true(self):
        car = Car()
        car.start()
        self.assertEqual(car.started, True)

    def test_stop_started_false(self):
        car = Car()
        car.stop()
        self.assertEqual(car.started, False)

    def test_start_stop_started_false(self):
        car = Car()
        car.start()
        car.stop()
        self.assertEqual(car.started, False)


if __name__ == '__main__':
    unittest.main()
