'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.'''

while True:
    str_topping = input("Enter the pizza topping that you would like to add: ")

    if str_topping == "quit":
        break
    else:
        print(f"{str_topping} will be added to your pizza")

