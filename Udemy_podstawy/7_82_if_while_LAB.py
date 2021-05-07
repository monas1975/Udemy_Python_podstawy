if __name__ == '__main__':
#1
    numbers =  [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

    i=0
    i_max = len(numbers)-1

    while i<i_max:
        print(i,numbers[i],numbers[i+1])
        if numbers[i]**2 == numbers[i+1]:
            print('t\Found',numbers[i],numbers[i+1])

        i+=1

#2
    print('-----------------------------')
    i=0
    i_max = len(numbers)-2
    while i < i_max:
        print(i, numbers[i], numbers[i + 1], numbers[i+2])
        if numbers[i] ** 2 == numbers[i + 1] and numbers[i + 1]**2 ==numbers[i+2]:
            print('t\Found', numbers[i], numbers[i + 1],numbers[i+2])
        print('i=',i)
        i+=1
    print('-------------xxxxxxxxxxxxxxxxxx------')
#3
    texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    n=0
    n_max = len(texts)-1
    print(n_max)
    print('========================')
    while n < n_max:
        print(n,texts[n],texts[n+1])
        if len(texts[n]) == len(texts[n+1]):
            print('t\Found ',texts[n],texts[n+1])
        n +=1
