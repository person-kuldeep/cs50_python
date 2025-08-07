'''
# INT

# take input from user
x = input("Enter x's value: ")
y = input("Enter y's value: ")

# do the conversion
x = int(x)
y = int(y)

# do calculation
sumition = x + y
subtraction = x - y
multiplication = x * y
division = x / y

# print the result 

print(f"Sum x+y: {sumition} ")
print(f"Subtraction x-y : {subtraction} ")
print(f"Multiplication x*y: {multiplication} ")
print(f"Division x/y: {division} ") 

'''

# FLOAT and Round

# get the user's input
x = float(input("Enter value for x: "))
y = float(input("Enter value for y: "))

# calculation
 
averageround  = (x + y) /2 

#print the result
print(f"Average of x and y: {round(averageround,3)} ")
print(f"Average of x and y: {averageround:.3f} ") # if after the decimal there is no number it will print zeros in till we wanted 
