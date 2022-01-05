class Restaurant:
    # Create class Restaurant

    # Initialize restaurant name and cuisine_type
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    # Description restaurant
    def describe_restaurant(self):
        print(f"This restaurant has name {self.restaurant_name}")
        print(f"{self.restaurant_name} restaurant has {self.cuisine_type}")

    # Open restaurant status
    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is Open !!!")

    def set_number_served(self, number_served):
        # Set number restaurant served
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print("the customer served can't negative")
    
    def increment_number_served(self, number_served):
        if number_served >= 0:
            self.number_served += number_served
        else:
            print("The increment served number can't negative")

    def read_number_served(self):
        print(f"{self.restaurant_name} served {self.number_served} customers.")

my_restaurant = Restaurant("Hoang Long", 'seafood')
your_restaurant = Restaurant("Da Sac Mau", 'BBQ')
his_restaurant = Restaurant("Nam Trung Bo", 'Mon Viet')

my_restaurant.describe_restaurant()
# your_restaurant.describe_restaurant()
# his_restaurant.describe_restaurant()

my_restaurant.read_number_served()
my_restaurant.set_number_served(10)
my_restaurant.read_number_served()
my_restaurant.increment_number_served(-10)
my_restaurant.read_number_served()