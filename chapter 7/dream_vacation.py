vacation = {}

active = True
while active:
    name = input("What is your name? ")
    place = input("If you could visit someplace in the world where would you go? ")

    vacation[name] = place

    response = input("Do you have anyone else that wants to participate? Please enter 'yes' or 'no'. ")
    if response == "no":
        active = False

for name, place in vacation.items():
    print(f"{name.title()} would like to go to {place}.")    