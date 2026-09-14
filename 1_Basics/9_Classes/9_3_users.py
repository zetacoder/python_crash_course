"""
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 

Make a method called describe_user() that prints a summary of the user's information. 

Make another method called greet_user() that prints a personalized greeting to the user.

Create several instances representing different users, and call both methods for each user.
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


user = Users("F", "L", age = 10, height = 50, weight = 30)

user.describe_user()

user.greet_user()


user_1 = Users("F1", "L1", age = 100, height = 500, weight = 300)

user_1.describe_user()

user_1.greet_user()

            

        