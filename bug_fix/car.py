
class Car:
    def __init__(self):
        self.cars = []  # Initialize an empty list to store cars

    def add_car(self, make, model):
        """Method to add a car to the list and return the index (car ID)."""
        self.cars.append((make, model))
        return len(self.cars) - 1  # Return the index of the added car

    def get_car(self, car_id):
        """Method to retrieve a car's make and model by its ID."""
        if car_id >= len(self.cars):
            return 'There is no such car'  # Return a message if car ID is out of range
        else:
            make, model = self.cars[car_id]
            return f'{make} {model}'  # Return the car's make and model

# Script demonstrating how to use the Car class
if __name__ == '__main__':
    car_lot = Car()
    car_id = car_lot.add_car('Toyota', 'Camry')
    print(f'Car Toyota Camry has been added with ID {car_id}')
    print(f'Car associated with ID {car_id} is {car_lot.get_car(car_id)}')
