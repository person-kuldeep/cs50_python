def main():
    name = input("Enter Name: ")
    print(hello(name))


def hello(to="World"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()
