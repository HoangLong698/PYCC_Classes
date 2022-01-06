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
    
    def fill_gas_tank(self):
        print("The car has a full tank of gas")

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


# my_bmw = Car('BMW', 'i8','2021')
# print(my_bmw.get_descriptive_name())
# my_bmw.fill_gas_tank()

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# # my_tesla.read_odometer()
# # my_tesla.update_odometer(20)
# # my_tesla.read_odometer()
# my_tesla.battery.describe_battery()

my_vinfast = ElectricCar('Vinfast', 'VF8', 2021)
print(my_vinfast.get_descriptive_name())
my_vinfast.battery.describe_battery()
# my_vinfast.fill_gas_tank()
my_vinfast.battery.get_range()
my_vinfast.battery.upgrade_battery()
my_vinfast.battery.describe_battery()
my_vinfast.battery.get_range()