"""

8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.


"""

def build_profile(first, last, **user_details):

    user_profile = {}

    user_profile['FirstName'] = first
    user_profile['LastName'] = last

    for key, value in user_details.items():
        user_profile[key] = value


    return user_profile


my_profile = build_profile("Amit", "Singh", Age = 0, height = 100, weight = 50, planet = "Earth")




