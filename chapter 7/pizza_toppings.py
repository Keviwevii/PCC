prompt = "Enter a topping that you want to add to the pizza. "
prompt += "Enter 'quit' when you are done."

active = True
while active:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Adding {topping}!")
    else:
        break