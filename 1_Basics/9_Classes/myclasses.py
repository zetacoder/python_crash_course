class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, numbers_served=0):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = numbers_served

    def set_number_served(self, numbers_served):
        self.numbers_served = numbers_served

    def increment_number_served(self, numbers_increased):
        self.numbers_served += numbers_increased

    def describe_retaurant(self):
        print(f"Name of the restaurant is {self.restaurant_name} and cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")



class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, numbers_served=0):
        super().__init__(restaurant_name, cuisine_type, numbers_served)
        self.flavors = ['F1', 'F2', 'F3', 'F4', 'F5']

    def desc_flavors(self):

        print("Ice cream flavors are: ")

        for flavor in self.flavors:
            print(f"     . {flavor}")


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