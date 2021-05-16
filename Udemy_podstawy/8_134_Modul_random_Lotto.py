import random

if __name__ == '__main__':
    myNumbers =[]

    while len(myNumbers)<7:
        newNumber = random.randint(1,49)


        if newNumber in myNumbers:
            print(("Elimineted:", newNumber))
            continue
        myNumbers.append(newNumber)

    print("Moje numery: ",myNumbers)