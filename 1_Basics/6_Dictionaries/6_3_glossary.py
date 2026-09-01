"""
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""
glossary = {
             "for loop" : "For loop helps in creating iteration of repetitive tasks",
             "items()" : "items() returns a sequence of key value pair stored within the python dictionary",
             "keys()" : "keys() returns the sequence of all the keys stored within a python dictionary",
             "value()" : "value() returns the sequence of all the values stored within a python dictionary",
             "set()" : "set is hybrid of list and dictionary and it only returns unique items stored",
           }

for word, meaning in glossary.items():
    print(word, ":", meaning)

