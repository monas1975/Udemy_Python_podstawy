import random
if __name__ == '__main__':

    for i in range(32,127):
        print((i,chr(i)))

    ints = range(33, 127)
    password =''

    for i in range(16):
        password +=chr(random.choice(ints))

    print(password)