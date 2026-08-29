str_guest_list = ["person_1", "person_2", "person_3"]

print(str_guest_list.pop(1))

str_guest_list.insert(1, "person_4")

str_messages_list = f"{str_guest_list[0]}, would you like to join me for dinner? \n{str_guest_list[1]}, would you like to join me for dinner? \n{str_guest_list[2]}, would you like to join me for dinner?"

print(str_messages_list)

print("I have found a bigger table")

str_guest_list.insert(0, "person_5")

str_guest_list.insert(2, "person_6")

str_guest_list.append("person_7")

for str in str_guest_list:
    print(str)


print("New dinner table won't be available, therefore only 2 guests will be invited")

while 1 == 1:

    removed_guest = str_guest_list.pop()

    print(f"{removed_guest}, sorry I can't invite you for dinner anymore")

    if(len(str_guest_list) == 2):
        break

print(f"Total {len(str_guest_list)} guests are invited for dinner")







    