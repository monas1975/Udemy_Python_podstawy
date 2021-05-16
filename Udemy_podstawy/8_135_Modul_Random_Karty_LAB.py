import random

if __name__ == '__main__':
    colors = ['Hearts','Diamonds','Clubs','Spades']
    figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']

    allCards =[]

    for color in colors:
        for figure in figures:
            card = color + " " + figure
            allCards.append(card)

    print(allCards)

    random.shuffle(allCards)

    print(allCards)

    player1 =[]
    player2 = []
    max = len(allCards)

    for i in range(0,max-1):
        if i%2==0:
            player1.append(allCards[i])
        else:
            player2.append(allCards[i])

    print("player1: ",player1)
    print("player2: ", player2)

    player3=allCards[:12]
    player4=allCards[12:]

    print("player3: ",player3)
    print("player4: ",player4)




'''
    for i in range(len(allCards)):
        print(allCards[i])
        print('\n')
'''

