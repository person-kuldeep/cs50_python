# match case 
'''
def process_command(command):
    match command:
        case ("move", x, y):
            print(f"Moving to ({x}, {y})")
        case ("say", message):
            print(f"Saying: {message}")
        case ("quit",):
            print("Quitting...")
        case {"action": "login", "user": user}:
            print(f"Logging in user: {user}")
        case _:
            print("Unknown command")

# Example usages:
process_command(("move", 10, 20))
process_command(("say", "Hello!"))
process_command({"action": "login", "user": "alice"})
process_command(("quit",))

'''
# get the anime name using character name
i = input("Enter favorite anime character: ")

match i:
    case "Luffy" | "Zoro" | "Nico Robin" | "Sanji":
        print("One Piece")
    case "Naruto" | "Jiraya" | "Kakashi":
        print("Naruto")
    case "Goku" | "Vegeta" | "Gohan":
        print("Dragon Ball")
    case _:
        print("Unknown anime character")



