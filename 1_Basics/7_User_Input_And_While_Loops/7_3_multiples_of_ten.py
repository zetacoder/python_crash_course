'''Ask the user for a number, and then report whether the number is a multiple of 10 or not.'''

int_number = int(input("Enter a number: "))

if int_number % 10 == 0:
    print(f"{int_number} is multiple of 10")
else: 
    print(f"{int_number} is not multiple of 10")