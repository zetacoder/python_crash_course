'''
Write a program that polls users about their dream vacation. 

Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll

'''

dict_poll_result = {}


while True:

    username = input("Enter the user name:")

    dict_poll_result[username] = input("Enter the place you would want to visit: ")

    if input("Enter 'Y' if you would like this poll to continue: ") == "Y":
        continue
    else:
        break

for username, place in dict_poll_result.items():
    print(f"{username.title()} would like to visit {place.title()}.")
