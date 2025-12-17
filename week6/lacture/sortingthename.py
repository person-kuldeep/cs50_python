names = []
with open("name.txt", "r") as file:
    for lines in file:
        names.append(lines.rstrip().title())
for name in sorted(names):
    print(f"Hello, {name}")

    