def main():
    student = get_student()
    if student["name"] == "Jack Sparrow":
        student["pirate"] = "Black Pearl"
    print(student["name"],"FROM",student["pirate"])

def get_student():
    name = input("Name: ")
    pirate = input("House: ")

    # # even without parentheses, it's still a tuple
    # return name, house 
    return {"name": name, "pirate": pirate} 
if __name__ == "__main__":
    main()