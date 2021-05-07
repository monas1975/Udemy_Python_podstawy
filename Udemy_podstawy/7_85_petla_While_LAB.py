import random
if __name__ == '__main__':

  #1

    i=0
    i_max = 50

    while i<=i_max-1:
        print(i , ' + ',i+1,' = ', i+(i+1))
        i+=1


    #2
    my_random = random.randint(0,20)
    ifCorrectNumber = False
    guess = -1
    trials = 0
    print(my_random)

    while guess != my_random:
        print("podaj loczbe:")
        guess = int(input())
        print('podales:',guess)
        trials+=1
        if guess == my_random:
            print('wygrales, zgadles za',trials,' -razem')