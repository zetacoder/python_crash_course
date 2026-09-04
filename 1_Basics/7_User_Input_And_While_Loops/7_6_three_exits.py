'''
Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:

Use a conditional test in the while statement to stop the loop.

Use an active variable to control how long the loop runs.

Use a break statement to exit the loop when the user enters a 'quit' value.

'''

is_true = True

while is_true:
    str_topping = input("Enter the pizza topping that you would like to add: ")

    if str_topping == "quit":
        is_true = False
    else:
        print(f"{str_topping} will be added to your pizza")