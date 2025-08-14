emote = ":)"

def main():
    global emote # Declare emote as global to modify it
    comment("helllooo evryone")
    emote = ":(" # This will not affect the global emote variable
    comment("sorry for the delay")


def comment(phrase):
    print( phrase + " " + emote)

main()


# we are using a global variable here, but it is not recommended to use global variables in this way.
# we can use the return value in other functions or print it.