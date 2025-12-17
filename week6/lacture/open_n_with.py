name = input("Enter name: ")
with open("name.txt", "a") as file:
    file.write(f"{name}\n")

with open("name.txt", "r") as file_r:
    lines = file_r.readlines()
    for line in lines:
        print(line , end="")
    

