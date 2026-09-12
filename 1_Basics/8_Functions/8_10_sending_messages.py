"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 

Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it's printed. 

After calling the function, print both of your lists to make sure the messages were moved correctly.

"""

def send_messages(messages, sent_messages):

    while messages:

        message = messages.pop()

        sent_messages.append(message)

sent_messages = []

messages = [
                         "This is text message 1",
                         "This is text message 2",
                         "This is text message 3",
                         "This is text message 4"
]

send_messages(messages, sent_messages)

print(f"Following are the messages in list of messages: ")

for message in messages:
    print(f"   . {message}")


print(f"Following are the messages in list of sent_messages")

for sent_message in sorted(sent_messages):
    print(f"   . {sent_message}")