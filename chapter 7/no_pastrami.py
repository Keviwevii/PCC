sandwich_orders = ["pastrami","club", "turkey", "pastrami", "ham", "BLT", "pastrami"]

print("Sorry we are all out of pastrami!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("\nHere are the current sandwiches that we have: ")
for sandwich in sandwich_orders:
    print(f"{sandwich.title()}")