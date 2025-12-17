import csv
"""
strawhats = []
with open("strawhats.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        strawhat =  {"name": row["fname"].strip(), "position": row["position"].strip()}
        strawhats.append(strawhat)

for member in sorted(strawhats, key=lambda member: member["name"]):
    print(f"{member['name']} is the {member['position']} of the Strawhat Pirates.")        
"""
name = input("Enter the name of the new crew member: ")
position = input("Enter their position on the ship: ")  

with open ("strawhats.csv", "a",newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["fname", "position"])
    # writer.writeheader()
    writer.writerow({"fname": name, "position": position})

print(f"{name} has been added as the {position} of the Strawhat Pirates.")
