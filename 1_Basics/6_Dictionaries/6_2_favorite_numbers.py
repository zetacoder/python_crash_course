"""
Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. 
Think of a favorite​ number for each person, and store each as a value in your dictionary. 
Print each person's name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

"""
favorite_numbers = {
                        "person_1" : 3,
                        "person_2" : 2,
                        "person_3" : 6,
                        "person_4" : 7
                   }

for person, favorite_number in favorite_numbers.items():
    print(f"{person}'s favorite number is {favorite_number}")