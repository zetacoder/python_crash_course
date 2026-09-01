"""
Use the code in favorite_languages.py (page 96).

Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.

Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

"""

favorite_languages = {
                        'jen' : 'python',
                        'sarah' : 'c',
                        'edward' : 'rust',
                        'phil' : 'python',

}

poll_participants = ['jen', 'den', 'ghen', 'edward', 'wah_edward', 'gazab_edward']

for person in poll_participants:
    if (person in favorite_languages.keys()):
        print(f"Thanks you, {person.title()} for taking the poll")
    else:
        print(f"Hi {person.title()}, I invite you to take the poll.")
