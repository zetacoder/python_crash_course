# 10-13. User Dictionary: The remember_me.py example only stores one piece of information, the username. 
# 
# Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary. 
# 
# Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). Print a summary showing exactly what your program remembers about the user.

from pathlib import Path
import json

def save_data_to_file(path, user_name, age, location):

    user_details = {"user_name": user_name, "age" : age, "location" : location}

    json_string = json.dumps(user_details)

    path.write_text(json_string)


def read_data_from_file(path):

    json_string = path.read_text() 

    user_details = json.loads(json_string)

    print(f"I remember you, {user_details['user_name']}, your age is {user_details['age'].title()} and location is {user_details['location']}.")


path = Path("1_Basics/10_Files_And_Exceptions/data_files/user_details.txt")

user_name = input("Enter the user name: ")

if path.exists():
    
    read_data_from_file(path)

else:

    age = input("Enter the age: ")

    location = input("Enter the location: ")

    save_data_to_file(path, user_name, age, location)






    



