rivers = {'Nile': "Egypt", "Mississippi": "United States", "Amazon": "Brazil"}

for river, country in rivers.items():
    if country == "United States":
        print(f"The {river} river runs through the {country}.\n")
    else:
        print(f"The {river} river runs through {country}.\n")

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)