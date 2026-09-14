"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 

Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 

Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several times. 

Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 

Print login_attempts again to make sure it was reset to 0.
"""


class Users:

    def __init__(self, first_name, last_name, **attr):

        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

        self.profile = {"name": self.first_name + " " + self.last_name}

        for key, value in attr.items():

            self.profile[key] = value


    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):

        print(f"Summary of the {self.first_name} {self.last_name} profile: ")

        for key, value in self.profile.items():
            if (key != "name"):
                print(f"     . {key.title()} of {self.first_name} {self.last_name} is {value}")

        print("Login attempts: ", self.login_attempts)


    def greet_user(self):

        print(f"Hello, {self.first_name} {self.last_name}!")


user = Users("F", "L", age = 10, height = 50, weight = 30)

user.describe_user()

user.increment_login_attempts()

user.increment_login_attempts()

user.increment_login_attempts()

user.increment_login_attempts()

user.increment_login_attempts()

user.describe_user()

user.reset_login_attempts()

user.describe_user()


            


        