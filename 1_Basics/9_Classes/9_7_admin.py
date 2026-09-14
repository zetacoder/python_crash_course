"""
9-7. Admin: An administrator is a special kind of user. 

Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). 

Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 

Write a method called show_privileges() that lists the administrator's set of privileges. 

Create an instance of Admin, and call your method.

"""

class Users:

    def __init__(self, first_name, last_name, **attr):

        self.first_name = first_name
        self.last_name = last_name

        self.profile = {"name": self.first_name + " " + self.last_name}

        for key, value in attr.items():

            self.profile[key] = value

    def describe_user(self):

        print(f"Summary of the {self.first_name} {self.last_name} profile: ")

        for key, value in self.profile.items():
            if (key != "name"):
                print(f"     . {key.title()} of {self.first_name} {self.last_name} is {value}")


    def greet_user(self):

        print(f"Hello, {self.first_name} {self.last_name}!")


class Admin(Users):

    def __init__(self, first_name, last_name, **attr):

        super().__init__(first_name, last_name, **attr)

        self.privileges = ["can add post", "can delete post", "can ban user"]


    def list_privileges(self):

        print("Following are the privileges granted to Admin user: ")

        for privilege in sorted(self.privileges):

            print(f"    . {privilege.title()}")


admin_1 = Admin("First", "Last", age = 10, height = 50, weight = 30)

admin_1.describe_user()

admin_1.list_privileges()