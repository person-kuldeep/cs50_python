l_yell = ["what", "is", "happenning","here"]
l_yell2 = ["hat", "is", "happy","here"]

l_int = [1,2,3,4,5,6,7,8,9,0]


def main():
    
    print(*map(lambda s, r : s.upper() + r.capitalize(),l_yell, l_yell2))
    print(*map(lambda n : pow(n,5),l_int))

    print(__name__)



if __name__ == "__main__":
    main()
