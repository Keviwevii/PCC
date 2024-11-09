mistoffelees = {
    "name": "Mistoffelees",
    "type": "cat",
    "owner": "Wilfredo",
}

jasmine = {
    "name": "Jasmine",
    "type": "cat",
    "owner": "Wilfredo",
}

charlie = {
    "name": "Charlie",
    "type": "cat",
    "owner": "Ashley",
}

animals = [mistoffelees, jasmine, charlie]

for animal in animals:
    print(f"{animal["name"]} is a {animal["type"]} and they are owned by {animal["owner"]}.\n")