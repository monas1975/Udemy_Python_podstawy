import datetime

if __name__ == '__main__':

#1
    lajk =1000
    lajkLimit =500
    udostepnienia = 101
    udostepnienieLimit = 100

    if lajk >= lajkLimit and udostepnienia >= udostepnienieLimit:
        print("promocja mozliwa")
    else:
        print("prmocja niemozliwa")

#2

    isPizzaOrdered = False
    isBigDrinkOrdered = False
    isWeekend = False

    if isPizzaOrdered and isBigDrinkOrdered and isWeekend:
        print("otrzymujesz kupon na burgera")
    else:
        print("kup wiecej")

#3
    diskSize =140
    diskSizeUsed = 123
    fileSize = 10
    if fileSize < (diskSize -diskSizeUsed):
        print("plik moze zostac pobrany")
    else:
        print("zbyt malo miejsca na dysku, by pobrac plik")


