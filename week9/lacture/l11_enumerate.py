fruits = ["apple", "banana", "mango"]
word = "python"


def main():
    print("Example 1: Default start (0)")
    for i, fruit in enumerate(fruits):
        print(i, fruit)

    print("\nExample 2: Start from 1")
    for i, fruit in enumerate(fruits, start=1):
        print(i, fruit)

    print("\nExample 3: Enumerate a string")
    for i, ch in enumerate(word):
        print(i, ch)

    print("\nExample 4: enumerate() is an iterator (lazy)")
    e = enumerate(["a", "b"], start=1)
    print(list(e))
    print(list(e))


if __name__ == "__main__":
    main()
