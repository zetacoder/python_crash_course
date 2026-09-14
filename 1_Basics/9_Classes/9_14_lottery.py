"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 

Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.

"""

from random import randint

lst_series = [1,34,56,65,3,2,7,545,23,4,"e","h","f","s","y"]

print("Any ticket matching these 4 numbers or letters wins a prize: ")

ct = 4

while ct > 0:

    random_element = lst_series.pop(randint(1, len(lst_series)) - 1)

    print(f".{random_element}")

    ct -= 1