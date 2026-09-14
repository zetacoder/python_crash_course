"""
9-12. Multiple Modules: 

Store the User class in one module, and store the Privileges and Admin classes in a separate module. 

In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

"""

import module_privilege_admin as p

admin_1 = p.Admin("First", "Last", age = 10, height = 50, weight = 30)


admin_1.privilege.list_privileges()