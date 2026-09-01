"""
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary's keys and values. 
When you're sure that your loop works, add five more Python terms to your glossary. 
When you run your program again, these new words and meanings should automatically be included in the output.

"""

glossary = {
             "for loop" : "For loop helps in creating iteration of repetitive tasks",
             "items()" : "items() returns a sequence of key value pair stored within the python dictionary",
             "keys()" : "keys() returns the sequence of all the keys stored within a python dictionary",
             "value()" : "value() returns the sequence of all the values stored within a python dictionary",
             "set()" : "set is hybrid of list and dictionary and it only returns unique items stored",
             "if" : "This enables decision making within the code",
             "else": "Provides a default option in the code decision making if no conditions are met",
             "elif" : "These help in adding more conditional decisions within the if clause",
             'list': "Number sequence of values of all types",
             'tuple': "Immutable list with initialization as (3,)"


           }

for word, meaning in glossary.items():
    print(word, ":", meaning)

