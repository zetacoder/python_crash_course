"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). 

Store the classes User, Privileges, and Admin in one module. 

Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

"""

import myclasses as m

admin_1 = m.Admin("First", "Last", age = 10, height = 50, weight = 30)


admin_1.privilege.list_privileges()