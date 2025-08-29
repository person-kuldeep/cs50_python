# conditions
# agree for the insurance policy
"""
s = input("did you approve for the policy? (y/n): ")
if s == 'y':
    print("you can get the insurance")  
elif s == 'n':
    print("you cannot get the insurance")
else:
    print("invalid input")        

"""
# your grade is
"""
g = int(input("enter your grade: "))

if g >= 90:
    print("A")
elif g >= 80:
    print("B")
elif g >= 70:
    print("C")
else :
    print("F")       
"""

# even or odd 

def main():
    n = int(input("enter a number: "))
    if is_even(n):
        print("even")
    else:
        print("odd")   


def is_even(x):
    #return True if x % 2 == 0 else False
    return x % 2 == 0

main()


