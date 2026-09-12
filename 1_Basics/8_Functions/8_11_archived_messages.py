"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 

After calling the function, print both of your lists to show that the original list has retained its messages.

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

send_messages(messages[:], sent_messages)

print(f"Following are the messages in list of messages: ")

for message in messages:
    print(f"   . {message}")


print(f"Following are the messages in list of sent_messages")

for sent_message in sorted(sent_messages):
    print(f"   . {sent_message}")