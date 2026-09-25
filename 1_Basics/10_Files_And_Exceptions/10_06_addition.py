# 10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
# When you try to convert the input to an int, you'll get a ValueError. Write a program that prompts lo two numbers. 
# Add them together and print the result. Catch the ValueError either input value is not a number, and print a friendly error message. 
# Test you program by entering two numbers and then by entering some text instead of a number.


try:
    input_1 = int(input("Enter the first numer: "))

    input_2 = int(input("Enter the second number:"))

except ValueError:
    print("Please enter a number and not a string")

else:

    print("Sum of the two numbers is -", str(input_1 + input_2))

