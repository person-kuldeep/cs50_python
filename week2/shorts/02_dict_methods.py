#create a dictionay where can add, access, and remove items
def main():
    dictone = {'home': 'place to stay', 'computer': 'machine to compute'}
    ctp = input("want to add, access, or remove the dict item? (a/ac/r): ").lower()
    if ctp == 'a' or ctp == 'add':
        word = input("Enter the word to add: ").lower()
        meaning = input("Enter the meaning of the word: ").lower()  
        dictone[word] = meaning
        print(f"Updated dictionary: {dictone}")
    elif ctp == 'ac' or ctp == 'access':
        word = input("Enter the word to access: ").lower()
        if word in dictone:
            print(f"The meaning of '{word}' is: {dictone[word]}")
        else:
            print(f"'{word}' not found in the dictionary.")
    elif ctp == 'r' or ctp == 'remove':
        word = input("Enter the word to remove: ").lower()
        if word in dictone.keys():
            delword =  dictone.pop(word)
            print(f"Removed '{word}' with meaning '{delword}' from the dictionary.")
            print(f"Updated dictionary after removal: {dictone}")
        else:
            print(f"'{word}' not found in the dictionary.")   
    else:
        print("Invalid choice. Please choose 'a', 'ac', or 'r'.")                

main()
