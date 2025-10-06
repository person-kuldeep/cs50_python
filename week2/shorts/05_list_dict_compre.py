#list comprehensions and dict comprehensions in Python

cubel = [x**3 for x in range(10)]
for a in cubel:
    print(f'cuberoot of {a} is {round(a**(1/3), 0)}') 

cubed = {x: x**3 for x in range(10)}

for k, v in cubed.items():
    print(f'cuberoot of {k} is {round(v**(1/3), 0)}')
