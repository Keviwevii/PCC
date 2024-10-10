pizza = ['pepperoni', 'cheese', 'sausage']

friend_pizzas = pizza[:]

pizza.append('pineapple')
friend_pizzas.append('plain')

print("My favorite pizzas are: ")
for pizza in pizza:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)