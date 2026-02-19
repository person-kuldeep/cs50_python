#set 
import random
n = int(input())
a = []

while n>0:
    n -= 1
    a.append(random.randrange(0,10))

b = set(a)
print({1,9} < b)
b.remove(9)

print(a,b)