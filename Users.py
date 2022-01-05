class Users:
    # Create Class Users

    # Initialize first_name and last_name
    def __init__(self, first_name, last_name, age, height, weight) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.name = first_name + ' ' +last_name
        self.login_attemps = 0

    # Creat a method describe user
    def describe_user(self):
        print(f"Your FirstName: {self.first_name}, LastName: {self.last_name}")
        print(f"{self.name} is {self.age} years old")
        print(f"{self.name}'s height is {self.height} cm and weight is {self.weight} kg")
    
    # Create a method welcome user
    def greet_user(self):
        print(F"Welcome to page {self.name}")
    
    def increment_login_attempts(self):
        # Add increment login by 1
        self.login_attemps += 1

    def reset_login_attempts(self):
        self.login_attemps = 0
    
    def print_login_attemps(self):
        print(f"{self.name} login attemps is {self.login_attemps}")

user1 = Users('Long', 'Tran', 21, 160, 60)
user2 = Users('John', 'Nguyen', 21, 175, 70)

user1.describe_user()
user2.describe_user()

user1.greet_user()
user2.greet_user()

print(f"User {user1.name} login attemps: {user1.login_attemps}")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.print_login_attemps()
user1.reset_login_attempts()
user1.print_login_attemps()