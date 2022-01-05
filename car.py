class Car:
    # A simple attempt to represent a car.

    def __init__(self, manufacturer, model, year) -> None:
        # Initilize attributes to describe a car.
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name.
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        # Print a statement showing the car's mileage.
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milege):
        # Set the odometer reading to the give value.
        # Reject the change if it attempts to roll the odometer back.
        if milege >= self.odometer_reading:
            self.odometer_reading = milege
        else:
            print("You can't roll back an odometer!!!.")
    
    def increment_odometer(self, milege):
        # Add the given amount to the odometer reading.
        if milege >= 0:
            self.odometer_reading += milege
        else:
            print("Milege can't negative number")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23 # Modify the attribute directly
# my_new_car.read_odometer()

my_new_car.update_odometer(10) # Modify the attribute through a method
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.update_odometer(10) # Can't not roll back odometer.

my_new_car.increment_odometer(10) # Increment odometer.
my_new_car.read_odometer()

your_car = Car('Honda', 'City', 2020)
print(your_car.get_descriptive_name())

your_car.odometer_reading = 10
your_car.read_odometer()
your_car.increment_odometer(-1000) # Milege increment can't negative
# your_car.read_odometer()