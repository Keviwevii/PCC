usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print(f"\nHello {user}, would you like to see a status report?")
        else:
            print(f"\nHello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")