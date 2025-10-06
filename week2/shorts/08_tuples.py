#tuples 
import sys 


loc = (-1, 2)
x, y = loc
print(f"x: {x}, y: {y}")
print(loc[0], loc[1])

print(sys.getsizeof(loc))  # size of tuple
print(sys.getsizeof([-1, 2]))  # size of list

print(sys.getsizeof(()))           # empty tuple
print(sys.getsizeof((1,)))         # 1 element
print(sys.getsizeof((1, 2, 3))) 