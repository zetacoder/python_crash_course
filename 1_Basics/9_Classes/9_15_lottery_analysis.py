"""
9-15. Lottery Analysis: 

You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 

Make a list or tuple called my_ticket. 

Write a loop that keeps pulling numbers until your ticket wins. 

Print a message reporting how many times the loop had to run to give you a winning ticket.

"""

from random import randint

lst_series = [1,34,56,65,3,2,7,545,23,4,"e","h","f","s","y"]

my_lottery = [34, 3, 7, "y"]

loop_count = 0

while True:

    loop_count += 1

    pool = lst_series[:]

    draw = []

    for _ in range(4):
        ix = randint(1, len(pool)) - 1

        draw.append(pool.pop(ix))

    if my_lottery == draw:
        print(f" {loop_count} times the loop had to run to give a winning ticket")
        break

