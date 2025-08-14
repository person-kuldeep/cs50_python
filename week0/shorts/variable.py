# Variable examples
def main():
    a = 10
    b = "hello"
    c = True

    d = "world"
    a = 20

    e = a + 10        # 30
    f = b + " " + d   # "hello world"
    g = c and True    # true
    h = not c         # false


    print(b + "" + d + str(a) )
    print( g, h )
    return a + 10 # return end of the function 

main()