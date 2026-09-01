"""
Use a dictionary to store information about a person you know Store their first name, last name, age, and the city in which they live. 
You should have keys such as first name, last name, age, and city. Print each piece of information stored in your dictionary.

"""
person = {
              'first_name' : 'Sachin',
              'last_name' : 'Tendulkar',
              'age' : 50,
              'city' : "Mumbai"
         }

for key, value in person.items():
    print(f"{key} of the person is {value}")




