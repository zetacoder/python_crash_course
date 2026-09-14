"""
9-1. Restaurant: Make a class called Restaurant. The _init_() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 

Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_retaurant(self):
        print(f"Name of the restaurant is {self.restaurant_name} and cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


restaurant = Restaurant("R1", "C1")


print(restaurant.restaurant_name, restaurant.cuisine_type)

restaurant.describe_retaurant()

restaurant.open_restaurant()