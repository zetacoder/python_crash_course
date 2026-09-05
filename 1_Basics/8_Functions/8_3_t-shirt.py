"""
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 

The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

"""

def make_shirt(size, message):

    print(f"T-Shirt has the size {size} and the message on this t-shirt: {message}")


make_shirt("Medium", "This is message 1")

make_shirt(message = "This is message 2", size="Large")
