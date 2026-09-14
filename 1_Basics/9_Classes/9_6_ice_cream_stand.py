"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 

Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). 

Either version of the class will work; just pick the one you like better. 

Add an attribute called flavors that stores a list of ice cream flavors. 

Write a method that displays these flavors. 

Create an instance of IceCreamStand, and call this method.

"""

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


obj_ics = IceCreamStand ('Ice Cream Stand 1', 'Ice Cream')

obj_ics.describe_retaurant()

obj_ics.desc_flavors()
