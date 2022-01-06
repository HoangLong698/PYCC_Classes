from users import Users
from admin import Admin

user1 = Users('Long', 'Tran', 21, 160, 60)
user2 = Users('John', 'Nguyen', 21, 175, 70)
user3 = Admin('John', 'Le', 23, 165, 80)

# user1.describe_user()
# user2.describe_user()
user3.describe_user()
user3.privileges.show_privileges()

print()
user1.greet_user()
user2.greet_user()
user3.greet_user()

# print(f"User {user1.name} login attemps: {user1.login_attemps}")
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.print_login_attemps()
# user1.reset_login_attempts()
# user1.print_login_attemps()