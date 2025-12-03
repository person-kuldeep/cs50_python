import s1_api_call
import sys
def main():
    if len(sys.argv) == 2:
        s1_api_call.find_titles(sys.argv[1])
    else:
        sys.exit("Please provide an artist name in quotation marks.")    

main()        