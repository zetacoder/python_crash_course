# 10-4. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

from pathlib import Path

path = Path("1_Basics/10_Files_And_Exceptions/guest.txt")

name = input("Enter your name: ")

if name:

    Path.write_text(path, name)