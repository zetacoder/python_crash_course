"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).

Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. 

Print the number of customers the restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who've been served. 

Call this method with any number you like that could represent how many customers were served in, say, a day of business.

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


restaurant = Restaurant("R1", "C1", 20)

print("numbers served: ", restaurant.numbers_served)

restaurant = Restaurant("R1", "C1", 50)

print("numbers served: ", restaurant.numbers_served)

restaurant.increment_number_served(30)

print("numbers served: ", restaurant.numbers_served)