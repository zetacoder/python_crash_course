"""
Make several dictionaries, where each dictionary represents a differ-ent pet. 

In each dictionary, include the kind of animal and the owner's name. 

Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.


"""
dict_pet1 = {"type": "dog", "owner": "owner_1",}

dict_pet2 = {"type": "cat", "owner": "owner_2"}

dict_pet3 = {"type": "goat", "owner": "owner_3"}

pets = [dict_pet1, dict_pet2, dict_pet3]

for pet in pets:
    print(f"{pet['owner']} has a pet and it is a {pet['type']}")


        