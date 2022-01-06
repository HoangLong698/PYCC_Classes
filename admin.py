from Users import Users
from privileges import Privileges 

class Admin(Users):
    # Initialize Admin Class inheritance from Users Class
    def __init__(self, first_name, last_name, age, height, weight) -> None:
        super().__init__(first_name, last_name, age, height, weight)
        self.privileges = Privileges()