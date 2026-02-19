import argparse

parser = argparse.ArgumentParser(prog="meaw.py", description="Meow n times")
parser.add_argument("-n", "--number", help="Number of times to meow", type=int, default=1)
parser.add_argument("-v", "--verbose", help="Verbose mode", action="store_true") #how this line works and for what?  
args = parser.parse_args() 

for _ in range(args.number):
    if args.verbose:
        print("MEOW")
    else:
        print("meow")


# import sys 

# if len(sys.argv) == 1:
#     print("meaw")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     print("meaw\n"*n, end="")
# else:
#     print("usage: meaw.py")
