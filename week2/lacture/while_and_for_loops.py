#While loops
#Where it repeats code while a condition is true

'''
x = 0
while x < 6:
    print("peer"),
    x += 1


while True:
    if x <=10
        print("infinite loop")
        continue
    else:
        print("break loop")
        break
    #break statement stops the loop
'''

#For loops
#Where it repeats code for a set number of times
'''
for _ in range(23):
    print("hht")

for i in range(5, 10):
    print(i)
'''
def main():
    attempt = 3
    while True:
        attempt -= 1
        passkey = input("Enter your passkey: ")
        if passkey == "secret":
            print("welcome")
            x = int(input("Enter your fav num: "))
            funprint(x)
            break
        elif attempt == 0:
            print("try after sometime")
            break

        else:
            print("try again")
            print("attempts left: ", attempt )
            continue
def funprint(b):
    
    for _ in range(b):
        print("#"*(b))  
        b -= 1  


main()        