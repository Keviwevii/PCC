wilfredo = {
    "first_name": "Wilfredo",
    "last_name": "Correa",
    "age": 34,
    "city": "Birmingham"
}

kevin = {
    "first_name": "Kevin",
    "last_name": "Floyd",
    "age": 29,
    "city": "Birmingham"
}

daphne = {
    "first_name": "Daphne",
    "last_name": "Allen",
    "age": "unknown",
    "city": "West Point"
}

users = [wilfredo,kevin,daphne]

for user in users:
    print(f"This is {user['first_name']} {user['last_name']}.")
    print(f"Their current age is {user["age"]}.")
    print(f"They currently live in {user["city"]}.\n")