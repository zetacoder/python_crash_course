"""
Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store all three dictionar-ies in a list called people. 

Loop through your list of people. As you loop through the list, print everything you know about each person.

"""

cricketer = {
              'first_name' : 'Sachin',
              'last_name' : 'Tendulkar',
              'age' : 50,
              'city' : "Mumbai"
            }

tennis_player = {
                   'first_name' : 'Roger',
                   'last_name' : "Federer",
                   'age' : 45,
                   'city' : 'Rapperswil‑Jona',
                }


pool_player = {
                 'first_name' : "Effren",
                 'last_name' : "Reyes",
                 'age' : 71,
                 'city' : 'Manila'
              }


sports_person = [cricketer, tennis_player, pool_player]


for player in sports_person:
    print()
    for key, value in player.items():
        print(f"{key.title()} is {value}")




