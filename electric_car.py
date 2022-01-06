""" A set of classes that can be used to represent electric cars."""

from car import Car

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