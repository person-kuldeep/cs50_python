# import gwc function from cowsay_mod module
import cowsay_mod
import sys
def main():
  if len(sys.argv) < 2:
    sys.exit("enter your name")
  else:
    cowsay_mod.gwc(sys.argv[1])

if __name__ == "__main__":
  main()