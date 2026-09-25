# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number.


while True:

    try:
        input_1 = int(input("Enter the first number: "))
        input_2 = int(input("Enter the second number: "))
        if input_1 == -5 or input_2 == -5:
            break
        else:
            print(f"Sum of the two numbers is - {input_1 + input_2}")
    except ValueError:
        pass


        
