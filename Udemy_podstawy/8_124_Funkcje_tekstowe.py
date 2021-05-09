
if __name__ == '__main__':

    line = 'this IS a very STRANGE text'
    print(line.capitalize())
    #print(line)
    print(line.title())

    print(line.upper())

    print(line.lower())

    print(line.swapcase())

    print(line.casefold())

    line2 ='ŻÓŁĆ'

    print(line2.upper())
    print(line2.lower())
    print(line2.casefold())

    print(line2.replace('Ż','Z').replace('Ó','O'))

    print(line.count('e'))

    print(line.find('e'))
    print(line.rfind('e'))
    print(line.index('e'))
    print(line.rindex('e'))

    print((line.find('p')))
    print('------------------------------')
    #print(line.index('p'))

    print(line.startswith('this'))
    print(line.startswith('This'))

    a = line.startswith('this')
    b = line.startswith('THIS')

    print(a)
    print(b)
