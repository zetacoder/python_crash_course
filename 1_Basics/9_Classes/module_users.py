class Users:

    def __init__(self, first_name, last_name, **attr):

        self.first_name = first_name
        self.last_name = last_name

        self.profile = {"name": self.first_name + " " + self.last_name}

        for key, value in attr.items():

            self.profile[key] = value

    def describe_user(self):

        print(f"Summary of the {self.first_name} {self.last_name} profile: ")

        for key, value in self.profile.items():
            if (key != "name"):
                print(f"     . {key.title()} of {self.first_name} {self.last_name} is {value}")


    def greet_user(self):

        print(f"Hello, {self.first_name} {self.last_name}!")