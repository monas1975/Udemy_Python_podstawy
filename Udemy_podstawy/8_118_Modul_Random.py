import random
if __name__ == '__main__':
    print("one randome number:",random.randint(1,100)) # od 1 do 100
    print('\n')

    print("choose randome number from range",random.choice(range(1,100)))
    print('\n')

    print("choose randome number from range", random.randrange(1,100))
    print('\n')

    list =["a","b","c","d","e","f"]
    print(list)
    random.shuffle(list)
    print(list)
    print('\n')

    print("just a random float", random.random())
    print('\n')




