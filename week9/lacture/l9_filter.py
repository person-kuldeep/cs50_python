students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


gryffindors = list(filter(lambda d: d["house"]== "Gryffindor", students))

for student in sorted(gryffindors, key=lambda x: x["name"]):
    print(student["name"])