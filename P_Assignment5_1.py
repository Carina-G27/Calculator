# Base class for a Superhero
class Superhero:
    def __init__(self, name, alias, strength, health):
        self._name = name  # Protected attribute for encapsulation
        self._alias = alias
        self._strength = strength
        self._health = health
        self._is_active = True  # Tracks if superhero is active (not defeated)

    # Getter for name (encapsulation)
    @property
    def name(self):
        return self._name

    # Setter for health with validation
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
            self._is_active = False
        else:
            self._health = value

    # Method to display superhero info
    def display_info(self):
        status = "Active" if self._is_active else "Defeated"
        return f"{self._alias} ({self._name}) | Strength: {self._strength} | Health: {self._health} | Status: {status}"

    # Method for performing a basic attack
    def attack(self, target):
        if self._is_active and target._is_active:
            print(f"{self._alias} attacks {target._alias} with strength {self._strength}!")
            target.health -= self._strength
            if not target._is_active:
                print(f"{target._alias} has been defeated!")
        elif not self._is_active:
            print(f"{self._alias} is defeated and cannot attack!")
        else:
            print(f"{target._alias} is already defeated!")

    # Method to heal the superhero
    def heal(self, amount):
        if self._is_active:
            self._health += amount
            print(f"{self._alias} heals for {amount}. New health: {self._health}")
        else:
            print(f"{self._alias} is defeated and cannot be healed!")

# Derived class for a Flying Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, strength, health, flight_speed):
        super().__init__(name, alias, strength, health)
        self._flight_speed = flight_speed  # New attribute specific to FlyingSuperhero

    # Getter for flight_speed
    @property
    def flight_speed(self):
        return self._flight_speed

    # Override display_info to include flight speed (polymorphism)
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} | Flight Speed: {self._flight_speed} km/h"

    # New method specific to FlyingSuperhero
    def fly_to_location(self, location):
        if self._is_active:
            print(f"{self._alias} flies to {location} at {self._flight_speed} km/h!")
        else:
            print(f"{self._alias} is defeated and cannot fly!")

    # Override attack to include a flying attack (polymorphism)
    def attack(self, target):
        if self._is_active and target._is_active:
            print(f"{self._alias} swoops down and attacks {target._alias} with strength {self._strength}!")
            target.health -= self._strength * 1.2  # Flying attack has 20% bonus
            if not target._is_active:
                print(f"{target._alias} has been defeated!")
        elif not self._is_active:
            print(f"{self._alias} is defeated and cannot attack!")
        else:
            print(f"{target._alias} is already defeated!")

# Example usage
if __name__ == "__main__":
    # Create a regular superhero
    hero1 = Superhero("Bruce Wayne", "Batman", 80, 100)
    print(hero1.display_info())

    # Create a flying superhero
    hero2 = FlyingSuperhero("Clark Kent", "Superman", 95, 150, 1000)
    print(hero2.display_info())

    # Demonstrate actions
    hero2.fly_to_location("Metropolis")
    hero1.attack(hero2)
    hero2.attack(hero1)
    hero2.heal(20)
    print(hero1.display_info())
    print(hero2.display_info())
    