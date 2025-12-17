strawhats = []
with open("strawhats.csv", "r") as file:
    for line in file:
        fname, lname, role = line.rstrip().split(",")
        strawhat = {"name": f"{lname} {fname}", "role": role}
        strawhats.append(strawhat)
# def name_key(strawhat):
#     return strawhat["name"]
for strawhat in sorted(strawhats, key=lambda strawhat: strawhat["name"]):
    print(f"{strawhat['name']} is {strawhat['role']}")
