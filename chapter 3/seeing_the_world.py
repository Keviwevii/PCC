places = ["Paris", "Greece", "Tokyo", "New York", "South Africa"]

print("The original list is below: ")
print(places)   

print("\nThe sorted list is below: ")
print(sorted(places))

print("\nThe original list is below: ")
print(places)

print("\nThe reserve sorted list is below: ")
print(sorted(places, reverse = True))

print("\nThe original list is below: ")
print(places)

print("\nThe reverse list is below: ")
places.reverse()
print(places)

print("\nThe original list is below: ")
places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)
