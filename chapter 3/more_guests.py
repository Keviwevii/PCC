guests = ["Zendaya", "Jennifer Lopez", "Oprah"]


print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")

print("I actually found a bigger table so 3 more guests will be invited.")

guests.insert(0, "Tom Cruise")
guests.insert(2, "Tom Holland")
guests.append("SZA")

print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")
print(f"Dear {guests[3]}, you are invited to dinner.")
print(f"Dear {guests[4]}, you are invited to dinner.")
print(f"Dear {guests[5]}, you are invited to dinner.")

