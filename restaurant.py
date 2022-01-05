class Restaurant:
    # Create class Restaurant

    # Initialize restaurant name and cuisine_type
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    # Description restaurant
    def describe_restaurant(self):
        print(f"This restaurant has name {self.restaurant_name}")
        print(f"{self.restaurant_name} restaurant has {self.cuisine_type}")

    # Open restaurant status
    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is Open !!!")

my_restaurant = Restaurant("Hoang Long", 'seafood')
your_restaurant = Restaurant("Da Sac Mau", 'BBQ')
his_restaurant = Restaurant("Nam Trung Bo", 'Mon Viet')

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
his_restaurant.describe_restaurant()