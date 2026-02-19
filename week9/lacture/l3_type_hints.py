def main()-> None:
    a = int(input("a: "))
    b: int = int(input("b: "))
    print(add_two_var(a,b))

def add_two_var(a:int,b:int)-> int:
    return a+b

def greet(name: str) -> str:
    """Takes a name (string) and returns a greeting (string)."""
    return f"Hello, {name}!"

def add(x: int, y: int) -> int:
    """Takes two integers and returns their sum."""
    return x + y

def process_items(items: list[str]) -> None:
    """Takes a list of strings and prints them. Returns nothing."""
    for item in items:
        print(item.upper())

def get_user_age(user_data: dict[str, int]) -> int | None:
    """
    Takes a dictionary where keys are strings and values are ints. 
    Returns an int (the age) OR None if 'age' is missing.
    """
    return user_data.get("age")


# Examples of usage
greeting = greet("Alice") 
# total = add("1", 2)  # This would be flagged by a type checker! 
process_items(["apple", "banana"])
age = get_user_age({"age": 30, "id": 101})

print(greeting)
print(age)