sandwich_orders = ["club", "turkey", "ham", "BLT"]
finished_sandwiches= []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich!")
    finished_sandwiches.append(current_sandwich)

print("\nThese were the sandwiches that were made: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")
