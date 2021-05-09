import random
if __name__ == '__main__':

#1. Zaimportuj moduł random
#2. 2. Wylosuj 10 liczb z zakresu 1-100

    for i in range(10):
        print(i,": ",random.randint(1,100))

#3
    number1 = random.randint(1,100)
    count = 0
    number2 = -1

    while number1 != number2:
        count+=1
        number2= random.randint(1,100)
        if number1 != number2:
            print(number1, " jest rozny od ",number2)
        else:
            print(number1, " jest rowny ",number2)

    print("poszukiwana liczba: ", number1, " zostala odgadnieta za ", count, " razem")

#4
    countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
    print(countries)
    print("-------------------------------------------")
    random.shuffle(countries)
    print(countries)

    groupNumber = 0

    for i in range(len(countries)):
        if i % 4 == 0:
            groupNumber+=1
            print("========== Group %d ==========" % (groupNumber))
        print(i,' : ',countries[i])

    print(len(countries))