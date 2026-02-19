l_yell = ["what", "is", "happenning","here"]
l_yell2 = ["hat", "is", "happy","here"]

l_int = [1,2,3,4,5,6,7,8,9,0]


def main():
    
    l1 = [_.upper() for _ in l_yell]
    l2 = [w.title() for w in l_yell2 if w.startswith("h") ]
    l3 = [w.title() if w.startswith("h") else w.lower() for w in l_yell2 ]
    print(*l2)
    print(*l3)

    print(__name__)



if __name__ == "__main__":
    main()