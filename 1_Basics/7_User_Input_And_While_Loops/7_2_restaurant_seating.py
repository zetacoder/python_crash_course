'''Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they'll have to wait for a table. Otherwise, report that their table is ready.'''

int_dinner_group_size = int(input("Enter the number of people in the group: "))

if int_dinner_group_size > 8:
    print("You'll have to wait for a table")
else:
    print("Your table is ready")
