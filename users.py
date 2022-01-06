class Users:
    # Create Class User
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

# class Privileges:
#     # Initialize Privileges Class
#     def __init__(self):
#         self.privileges = ['can add post', 'can delete post', 'can ban user', 'can grant permission']

#     # Show the privileges of instance of Admin class
#     def show_privileges(self):
#         print(f"The privileges of Administrator: ")
#         for privilege in self.privileges:
#             print(f"+ {privilege}")

# class Admin(Users):
#     # Initialize Admin Class inheritance from Users Class
#     def __init__(self, first_name, last_name, age, height, weight) -> None:
#         super().__init__(first_name, last_name, age, height, weight)
#         self.privileges = Privileges()