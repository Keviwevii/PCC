num_people = input("How many people will be dining today? ")
num_people = int(num_people)

if num_people > 8:
    print("Sorry, but you will have to wait for a table!")
else:
    print("Your table is ready!")