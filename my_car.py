
from electric_car import ElectricCar as EC
from car import Car 
# import electric_car


my_bmw = Car('bmw', 'i8', 2020)
print(my_bmw.get_descriptive_name())
my_bmw.odometer_reading = 23
my_bmw.read_odometer()

my_vinfast = EC('Vinfast', 'vf8', 2021)
print(my_vinfast.get_descriptive_name())
my_vinfast.battery.describe_battery()
my_vinfast.battery.get_range()