'''
def area(w,h):
    """Calculate the area of a rectangle."""
    width = w
    height = h
    print("area of the room is " + str(width * height) + " sq ft")  
'''
# Upper one hase no return value, so can't be used in other functions 

def area(w, h):
    """Calculate the area of a rectangle."""
    width = w
    height = h
    return width * height  # Return the calculated area

def main():

    home = area(w=10, h=20)  
    yard = area(5, 10)
    print("Area of home:", home, "sq ft")
    print("Area of yard:", yard, "sq ft")
     
main()     
    