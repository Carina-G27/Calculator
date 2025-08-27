# Base class for Vehicle
class Vehicle:
    def __init__(self, name, speed):
        self._name = name  # Protected attribute for encapsulation
        self._speed = speed

    # Getter for name
    @property
    def name(self):
        return self._name

    # Getter for speed
    @property
    def speed(self):
        return self._speed

    # Base move method to be overridden (polymorphism)
    def move(self):
        raise NotImplementedError("Subclasses must implement move() method")

    # Method to display vehicle info
    def display_info(self):
        return f"Vehicle: {self._name} | Speed: {self._speed} km/h"

# Derived class for Car
class Car(Vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    # Override move method for Car
    def move(self):
        return f"{self._name} is driving on the road at {self._speed} km/h! 🚗"

# Derived class for Plane
class Plane(Vehicle):
    def __init__(self, name, speed, altitude):
        super().__init__(name, speed)
        self._altitude = altitude

    # Getter for altitude
    @property
    def altitude(self):
        return self._altitude

    # Override move method for Plane
    def move(self):
        return f"{self._name} is flying in the sky at {self._speed} km/h and {self._altitude} meters altitude! ✈️"

# Derived class for Boat
class Boat(Vehicle):
    def __init__(self, name, speed, water_type):
        super().__init__(name, speed)
        self._water_type = water_type  # e.g., ocean, lake

    # Getter for water_type
    @property
    def water_type(self):
        return self._water_type

    # Override move method for Boat
    def move(self):
        return f"{self._name} is sailing on the {self._water_type} at {self._speed} km/h! ⛵"

# Example usage
if __name__ == "__main__":
    # Create different vehicles
    car = Car("Toyota Camry", 120)
    plane = Plane("Boeing 747", 900, 10000)
    boat = Boat("Yacht Serenity", 50, "ocean")

    # Store vehicles in a list to demonstrate polymorphism
    vehicles = [car, plane, boat]

    # Display info and movement for each vehicle
    for vehicle in vehicles:
        print(vehicle.display_info())
        print(vehicle.move())
        print()  # Empty line for readability