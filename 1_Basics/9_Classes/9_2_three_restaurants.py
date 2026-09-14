"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
"""
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_retaurant(self):
        print(f"Name of the restaurant is {self.restaurant_name} and cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


restaurant_1 = Restaurant("R1", "C1")

restaurant_2 = Restaurant("R2", "C2")

restaurant_3 = Restaurant("R3", "C3")

restaurant_1.describe_retaurant()

restaurant_2.describe_retaurant()

restaurant_3.describe_retaurant()
