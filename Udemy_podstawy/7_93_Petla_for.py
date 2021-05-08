if __name__ == '__main__':
    for number in range(20):
        print(number)

    for number in range(1,21):
        print(number)

    for number in range(1,21,2):
        print(number)

    for number in range(1,21):
        if number %2 == 0:
            print('Number %2d is %s'%(number,'even'))
        else:print('Number %2d is %s'%(number,'odd'))