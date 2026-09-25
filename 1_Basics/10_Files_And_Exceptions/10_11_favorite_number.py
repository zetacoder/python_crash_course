# 10-11. Favorite Number: Write a program that prompts for the user's favorite number. 
# 
# Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message "I know your favorite number! It's


from pathlib import Path

import json as j

def read_fav_number(path):

    fav_number = path.read_text()

    print(f"I know your favorite number! It's {fav_number}")


def write_fav_number(path):

    fav_number = int(input("Enter your favorite number: "))

    json_val = j.dumps(fav_number)

    path.write_text(json_val)







try:

    path = Path("1_Basics/10_Files_And_Exceptions/data_files/fav_num.txt")

    if path.exists(): 
        read_fav_number(path)
    else:
        write_fav_number(path)

except ValueError:
    print("Please enter a valid Integer")
    


