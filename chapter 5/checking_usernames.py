current_users = ["catlover23", "tigerking", "upsidedowncake33", "georgesantosfire", "john"]

new_users = ["JOHN", "sonicheadhog", "turtlefighter", "tigerking", "ladyfinger"]

new_users_copy = []

for user in new_users:
    new_users_copy.append(user.lower())

for user in new_users_copy:
    if user in current_users:
        print("This username is in use, please use a different one.")
    else:
        print("This username is available!")
