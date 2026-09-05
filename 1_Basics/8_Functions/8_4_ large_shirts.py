"""
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 

Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

"""


def make_shirt(size = "Large", message = "I Love Python"):

    print(f"T-Shirt has the size {size} and the message on this t-shirt: {message}")


make_shirt(size = "Medium")

make_shirt(size="Large")

make_shirt(message= "This is a different message")
