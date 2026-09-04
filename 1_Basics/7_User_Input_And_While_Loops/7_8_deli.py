'''
Make a list called sandwich_orders and fill it with the names of various sandwiches. 

Then make an empty list called finished_sandwiches. 

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. 

After all the sandwiches have been made, print a message listing each sandwich that was made.

'''

lst_sandwich_orders = ['s1', 's2', 's3', 's4', 's5', 's6']

lst_finished_sandwiches = []

while lst_sandwich_orders:

    sandwich = lst_sandwich_orders.pop()

    print(f"I made your {sandwich} sandwich")

    lst_finished_sandwiches.append(sandwich)

print("Final list of Sandwiches :")

for sandwich in sorted(lst_finished_sandwiches):
    print(sandwich)

