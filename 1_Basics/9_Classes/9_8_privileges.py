"""
9-8. Privileges: Write a separate Privileges class. 

The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 

Move the show_privileges() method to this class. 

Make a Privileges instance as an attribute in the Admin class. 

Create a new instance of Admin and use your method to show its privileges.

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


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def list_privileges(self):

        print("Following are the privileges granted to Admin user: ")

        for privilege in sorted(self.privileges):

            print(f"    . {privilege.title()}")


class Admin(Users):

    def __init__(self, first_name, last_name, **attr):

        super().__init__(first_name, last_name, **attr)      

        self.privilege = Privileges()



admin_1 = Admin("First", "Last", age = 10, height = 50, weight = 30)

admin_1.describe_user()

admin_1.privilege.list_privileges()



