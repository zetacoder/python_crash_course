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
