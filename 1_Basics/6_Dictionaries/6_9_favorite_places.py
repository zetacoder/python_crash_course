"""
Make a dictionary called favorite_places. 

Think of three​ names to use as keys in the dictionary, and store one to three favorite places for each person. 

To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person's name and their favorite places.

"""

favorite_places = {
                    "person_1": ["place_1", "place_2", "place_3"],
                    "person_2": ["place_2", "place_3", "place_4"],
                    "person_3": ["place_1", "place_4"],
}

for person in favorite_places:
    print(f"\n{person.title()} has favorites places as:  ")
    for place in favorite_places[person]:
        print(place, end = " ")
