# try except 
def main():
    outx = val("Enter an integer: ")
    print(f"You entered: {outx}")
def val(intx):
    while True:
        try : 
            return int(input(intx))
        except ValueError:
            print("That's not an integer!") 

main()        
   