from abc import ABC, abstractmethod

# 1. Define the Abstract Class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        """Abstract method: Subclasses must implement this."""
        pass

    def honk(self):
        """Concrete method: Subclasses inherit this automatically."""
        return "Beep beep!"

# 2. Try to instantiate the abstract class (This will fail)
# my_vehicle = Vehicle()  # Raises TypeError

# 3. Create a valid Subclass
class Car(Vehicle):
    def start_engine(self):
        return "Car engine roaring to life."

# 4. Create an invalid Subclass (Forgot to implement start_engine)
class Motorcycle(Vehicle):
    pass

# --- Testing the implementation ---
my_car = Car()
print(my_car.start_engine())  # Output: Car engine roaring to life.
print(my_car.honk())          # Output: Beep beep! (Inherited concrete method)

# This raises a TypeError because Motorcycle did not implement 'start_engine'
# my_bike = Motorcycle() 
