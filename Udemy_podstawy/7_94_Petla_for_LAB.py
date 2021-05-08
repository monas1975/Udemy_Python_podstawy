if __name__ == '__main__':
    string_A = '+---+---+---+---+'
    string_B = '|   |   |   |   |'

    for i in range(5):
        print(string_A)

    print('xxxxxxxxxxxxxxxxxxxxxxxxx')

    for i in range(1,9):
        if i % 2 == 0:
            print(string_B)
        else:
            print(string_A)

    print('xxxxxxxxxxxxxxxxxxxxxxxxx')

    for n in range(1,10):
        print("x"*n)

    print('xxxxxxxxxxxxxxxxxxxxxxxxx')

    for n in range(1,10):
        if n%2 == 0:
            print("x" * n)
        else:
            print("o" * n)

