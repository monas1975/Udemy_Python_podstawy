if __name__ == '__main__':
    #1
    data = ['Error:File cannot be open',
            'Error:No free space on disk',
            'Error:File missing',
            'Warning:Internet connection lost',
            'Error:Access denied']
    for i in data:
        print(i.upper())

    print('----------------------------------------')
    #2
    for n in data:
        splitList = n.split(':')
        print(splitList[0].upper())
        print(splitList[1])

    print('3==============================================')

    #3
    for n in data:
        splitList = n.split(':')
        print(splitList[0].upper())
        if splitList[0] == 'Error':
            print(splitList[1].upper())
        else:
            print(splitList[1])
     

