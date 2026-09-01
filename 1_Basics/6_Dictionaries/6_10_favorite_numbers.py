"""
Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. 

Then print each person's name along with their favorite numbers.
"""

favorite_numbers = {
                        "person_1" : [3, 23, 87],
                        "person_2" : [2, 288, 342],
                        "person_3" : [6, 600],
                        "person_4" : [7, 402, 655, 989],
                   }

for person, favorite_number in favorite_numbers.items():
    print(f"{person}'s favorite numbers are {favorite_number}")