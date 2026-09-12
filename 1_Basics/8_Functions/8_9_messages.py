"""
8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

"""


def show_messages(txt_msgs):

    for msg in txt_msgs:

        print(msg)


short_text_messages = [
                         "This is text message 1",
                         "This is text message 2",
                         "This is text message 3",
                         "This is text message 4"
]

show_messages(short_text_messages)