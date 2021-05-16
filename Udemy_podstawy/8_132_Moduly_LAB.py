import math
import random

if __name__ == '__main__':
    inputdata = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    factortable = [0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.13, 0.21, 0.34, 0.55, 0.89]

    print(len(inputdata))
    print(len(factortable))

    if len(inputdata) == len(factortable):
        print("--")
        for i in range(len(inputdata)):
            minvalue = inputdata[i]-factortable[i]*inputdata[i]
            maxvalue = inputdata[i]+factortable[i]*inputdata[i]
            print("minvalue: ", minvalue, " maxvalue: ",maxvalue)
            minint = math.floor(minvalue)
            maxint = math.ceil(maxvalue)
            print(minint,maxint)
    else:
        print("inputdata and factortable need to have equal number of elements")


    #2


    print("-----------------------------------------")
    for i in range(len(inputdata)):
        minvalue = inputdata[i] -  random.random()* inputdata[i]
        maxvalue = inputdata[i] + random.random() * inputdata[i]
        print("minvalue: ", minvalue, " maxvalue: ", maxvalue)
        minint = math.floor(minvalue)
        maxint = math.ceil(maxvalue)
        print(minint, maxint)

    #3
    import datetime
    print(datetime.datetime.today())
    print("%Y-%M-%D",datetime.datetime.today().strftime("%Y-%m-%d"))