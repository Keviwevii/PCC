favorite_languages = {
    'jen': "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

poll_takers = ["kevin", "jen", "lisa", "edward"]

for person in favorite_languages:
    if person in poll_takers:
        print(f"Hi {person.title()}, thank you for taking the poll!")
    else:
        print(f"Hi {person.title()}, please take the poll!")