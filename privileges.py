class Privileges:
    # Initialize Privileges Class
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can grant permission']

    # Show the privileges of instance of Admin class
    def show_privileges(self):
        print(f"The privileges of Administrator: ")
        for privilege in self.privileges:
            print(f"+ {privilege}")