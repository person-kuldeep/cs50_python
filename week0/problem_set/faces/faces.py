#defining convert func
def convert(i):
    i = str(i)
    o0 = i.replace(":)","🙂")
    o_final = o0.replace(":(","🙁")
    return o_final
#defining main func to take input and use convert func to change the str and print it
def main():
    user_inp = input("say some stuf : ")
    output_str = convert(user_inp)
    print(output_str)

# calling main func
main()


