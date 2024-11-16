prompt = "What is your age? I can let you know how much your ticket is. "
prompt += "\nEnter 'quit' when everyone is accounted for. "

active = True
while active: 
    age = input(prompt)
    if age != 'quit':
        age = int(age)

        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
    else:
        break

