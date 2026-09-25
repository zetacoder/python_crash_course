# 10-14. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. 
# 
# We should modify it in case the current user is not the person who last used the program.
#
# Before printing a welcome back message in greet_user(), ask the user if this is the correct username. 
# 
# If it's not, call get_new_username() to get the correct username.

from pathlib import Path
import json

def greet_user(user_details):
    print(f"I remember you, {user_details['user_name']}, your age is {user_details['age'].title()} and location is {user_details['location']}.")
    

def get_new_user_name(path, user_name):

    age = input("Enter the age: ")
    
    location = input("Enter the location: ")
    
    save_data_to_file(path, user_name, age, location)


def save_data_to_file(path, user_name, age, location):

    user_details = {"user_name": user_name, "age" : age, "location" : location}

    json_string = json.dumps(user_details)

    path.write_text(json_string)



def read_data_from_file(path, user_name):

    json_string = path.read_text() 

    user_details = json.loads(json_string)

    if user_details["user_name"] == user_name:
        greet_user(user_details)
    else:
        get_new_user_name(path, user_name)
        

    

path = Path("1_Basics/10_Files_And_Exceptions/data_files/user_details.txt")

user_name = input("Enter the user name: ")

if path.exists():
    
    read_data_from_file(path, user_name)

else:

    get_new_user_name(path, user_name)

    