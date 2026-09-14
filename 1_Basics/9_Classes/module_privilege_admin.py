import module_users as m


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def list_privileges(self):

        print("Following are the privileges granted to Admin user: ")

        for privilege in sorted(self.privileges):

            print(f"    . {privilege.title()}")


class Admin(m.Users):

    def __init__(self, first_name, last_name, **attr):

        super().__init__(first_name, last_name, **attr)      

        self.privilege = Privileges()