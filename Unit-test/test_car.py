
import unittest
from car import Car

class TestCar(unittest.TestCase):
    
    def setUp(self):
        """Set up a Car instance for each test."""
        self.car_lot = Car()

    def test_add_car(self):
        """Test adding a car and retrieving the car ID."""
        car_id = self.car_lot.add_car('Ford', 'Focus')
        self.assertEqual(car_id, 0)
        car_id = self.car_lot.add_car('Honda', 'Civic')
        self.assertEqual(car_id, 1)
    
    def test_get_car(self):
        """Test retrieving cars by car ID."""
        self.car_lot.add_car('Nissan', 'Altima')
        self.car_lot.add_car('Chevrolet', 'Malibu')
        
        # Test existing car IDs
        self.assertEqual(self.car_lot.get_car(0), 'Nissan Altima')
        self.assertEqual(self.car_lot.get_car(1), 'Chevrolet Malibu')
        
        # Test non-existent car IDs
        self.assertEqual(self.car_lot.get_car(2), 'There is no such car')

# Run the unit tests
if __name__ == '__main__':
        unittest.main()
