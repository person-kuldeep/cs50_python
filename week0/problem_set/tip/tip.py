def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
     # $##.## to ##.##
    d = str(d)
    out_dol_flo = float(d[1:])
    return out_dol_flo

def percent_to_float(p):
    #  ##% to ##
    p = str(p)
    out_per_flo = (float(p[:-1]))/100
    return out_per_flo

main()
