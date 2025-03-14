# CASE - 1 Print names starts with R
# CASE - 2 create a new list with only users starts with R
# CASE - 3 Removed names doesnt start with R

users = ["Rajesh", "Ramesh", "Mahesh","Dinesh", "Rakesh", "Anil"]

valid_users = ["Rajesh", "Anil"]

# CASE - 1 with for loop
for user in users:
    if user.startswith("R"):
        print(user)

# CASE - 1 with for list comprehensions       
# new_list = [user for user in users if user.startswith("R")]
# print(new_list)

new_list = []
# CASE - 2 with for loop
for user in users:
    if user.startswith("R"):
        new_list.append(user)


