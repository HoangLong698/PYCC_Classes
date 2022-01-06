""" A class that can be used to represent car """
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
        return long_name.title() # Return Uppercase first letter
    
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

class Battery:
    """ A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75) -> None:
        """ Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

    def get_range(self):
        """ Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on full charge.")
        
class ElectricCar(Car):
    """ Represent aspect of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year) -> None:
        ## Initialize attributes of the parent class.
        super().__init__(manufacturer, model, year)
        # Defing attributes for the Child Class
        # self.battery_size = 75 
        # Instance as attributes from Battery class
        self.battery = Battery() 

    # def describe_battery(self):
    #     """ Print a statement describing the battery size."""
    #     print(f"This car has a {self.battery_size}-kWh battery.")
    
    def fill_gas_tank(self):
        """ Electric cars don't have gas tank."""
        print("This car doesn't need a gas tank")