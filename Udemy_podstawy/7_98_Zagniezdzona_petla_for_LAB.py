if __name__ == '__main__':
    #1 Oblicz silnie
    i=4
    result = 1

    for j in range(1,i+1):
        result *=j

    print(i,result)

    print("-----------------------------")
#2
    n=5


    for i in range(1,n+1):
        result = 1
        for j in range(1,i+1):
            result *=j
        print(str(i) + '    ' + str(result))

    print("-----------------------------")
#3
    list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
    list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']


    for noun in list_noun:
         for adj in list_adj:
             print(noun+ ' ' + adj)


