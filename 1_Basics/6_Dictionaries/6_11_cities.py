"""
Make a dictionary called cities. Use the names of three cities as​ keys in your dictionary. 

Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 

The keys for each city's dictionary should be something like country, population, and fact. Print the name of each city and all of the infor-mation you have stored about it.
"""

dict_cities = {
                 "New York City": {"country": "United States","population" : 8584629, "Fact" :  "New York City is the largest city in the United States, with more than double the population of second‑place Los Angeles."},
                 "Los Angeles": {"country":"United States","population" : 3863148, "Fact" :  "Los Angeles is known for its massive urban sprawl, covering 471 square miles, making it one of the largest cities by land area in the U.S. "},
                 "Chicago": {"country":"United States","population" : 2727758, "Fact" :  "Chicago has one of the highest population densities in the U.S. at 11,977 people per square mile, reflecting its compact urban cor",},
              }

for city, details in dict_cities.items():
    print(f"Details of the city - {city} : ")

    for key, value in dict_cities[city].items():
        print(f"{key} = {value}")

