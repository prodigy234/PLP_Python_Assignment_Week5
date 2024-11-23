#Assignment 1: Design Your Own Class! 

# I created a class for a Smartphone with inheritance and encapsulation.

# Parent Class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Initialize parent class attributes
        self.__storage = storage       # Private attribute
        self.battery = battery

    # Encapsulation: Getter and Setter for storage
    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Storage must be positive!")

    # Method to simulate usage
    def use(self, hours):
        self.battery -= hours * 10
        return f"Battery remaining: {self.battery}%"

# Create an object of Smartphone
my_phone = Smartphone("Apple", "iPhone 14", 256, 100)

# Use the object
print(my_phone.device_info())  # Output: Apple iPhone 14
print(f"Storage: {my_phone.get_storage()} GB")  # Output: Storage: 256 GB
my_phone.use(3)
print(my_phone.use(3))  # Output: Battery remaining: 40%


# Activity 2: Polymorphism Challenge! 

# I defined classes for different vehicles with their own implementations of a common move() method.

# Parent Class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Child Class: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Child Class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Child Class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Function to demonstrate polymorphism
def vehicle_action(vehicle):
    print(vehicle.move())

# Create objects of each class
car = Car()
plane = Plane()
boat = Boat()

# Use polymorphism to call the same method on different objects
vehicle_action(car)    # Output: Driving 🚗
vehicle_action(plane)  # Output: Flying ✈️
vehicle_action(boat)   # Output: Sailing 🚢
