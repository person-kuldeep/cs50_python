'''
#define the hello function
def hello(to="buddy"):
    print(f"Hello, {to}!")
#take input from user of user's name 
user_name = input("who are you? ")
#exicute the function
hello(user_name)
'''
'''
#define the main function
def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="buddy"):
    print(f"Hello, {to}!")


main() # Call the main function to execute the program    
'''


def main():
    x = input("Enter the nunber: ")
    x = int(x)
    y = input("Enter the power for number: ")
    y = int(y)
    print(powerofnum(x, y)) 
     
def powerofnum(e, k):
    return pow(e, k)

main()