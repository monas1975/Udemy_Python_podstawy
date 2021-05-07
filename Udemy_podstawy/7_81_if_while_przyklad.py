if __name__ == '__main__':

    values=[10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]
    print('cc')

    i=0
    max = len(values)-2
    print(max)

    while i<max:
        print(i,values[i],values[i+1],values[i+2])

        if(values[i]<values[i+1] and values[i+1]<values[i+2]):
            print('\tFound: ',values[i],values[i+1],values[i+2])
        i+=1