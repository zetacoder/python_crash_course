'''
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 

Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 

Make sure no pastrami sandwiches end up in finished_sandwiches.

'''

lst_sandwich_orders = ['s1', 'pastrami', 's2', 's3', 's4', 'pastrami', 's5', 's6', 'pastrami', 'pastrami', 'pastrami']

lst_finished_sandwiches = []

print("Deli has run out of pastrami")

while 'pastrami' in lst_sandwich_orders:
    lst_sandwich_orders.remove('pastrami')

while lst_sandwich_orders:

    sandwich = lst_sandwich_orders.pop()

    print(f"I made your {sandwich} sandwich")

    lst_finished_sandwiches.append(sandwich)

print("Final list of Sandwiches :")

for sandwich in sorted(lst_finished_sandwiches):
    print(sandwich)