if __name__ == '__main__':

    countries = ['PL','FR','US','DE','RU']

    print(countries)

    print(countries[0])
    print(countries[1])
    print(countries[2])

    countries[3] ='GB'
    print(countries)

    countries.append('CAN')
    print(countries)
    countries.insert(2,'ES')
    print(countries)
    countries.remove('RU')
    print(countries)
    countries.sort()
    print(countries)
    countries.reverse()
    print(countries)
    print(countries.pop(2))
    print(countries)
    print(countries.index('PL'))
    print(countries.count('DE'))
    print(countries.count('PL'))

    newList = ['FI','SE']
    print(newList)
    countries.extend(newList)
    print(countries)

    countriesCopy = countries
    countriesCopy = countries.copy()
    print(countriesCopy)
    print(countries)

    countriesCopy.clear()

    print(countriesCopy)
    print(countries)
