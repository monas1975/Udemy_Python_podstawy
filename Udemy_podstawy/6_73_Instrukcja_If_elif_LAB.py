import datetime

if __name__ == '__main__':

#1
    lajk =100
    lajkLimit =500
    udostepnienia = 101
    udostepnienieLimit = 100

    if lajk >= lajkLimit and udostepnienia >= udostepnienieLimit:
        print("promocja mozliwa")
    elif lajk<lajkLimit:
        print("prmocja niemozliwa - zbyt malo lajkow")
    elif udostepnienia<udostepnienieLimit:
        print("zbyt malo udostepnien")

#2

    isPizzaOrdered = True
    isBigDrinkOrdered = True
    isWeekend = False

    if isPizzaOrdered and isBigDrinkOrdered and isWeekend:
        print("otrzymujesz kupon na burgera")
    elif not isPizzaOrdered:
        print("zamow pizza")
    elif not isBigDrinkOrdered:
        print("zamow duzy napoj")
    elif not isWeekend:
        print('to nie weekend')





