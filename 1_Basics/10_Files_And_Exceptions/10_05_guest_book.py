# 10-5. Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

from pathlib import Path

path = Path("1_Basics/10_Files_And_Exceptions/guest_book.txt")

names = ""

while True:

    name = input("Enter a name: ")

    if name.upper() == "N":
        break
    else:
        names = names + name + "\n"

Path.write_text(path, names)






