if __name__ == '__main__':

#1, Utwórz 3 zmienne
    musclePain = False
    fever = True
    weakness = True

#2
    if musclePain and fever and weakness:
        print("suspicion of influenza")
    else:
        print("the flue is unlikely")

#3
    if musclePain and fever and weakness:
        print("suspicion of influenza")
    elif weakness and (not fever and not musclePain):
        print("jus take a break")
    else:
        print("you may be cold")

#4
    isMan = True

#5
    if (musclePain and fever and weakness) or (isMan and (musclePain or fever or weakness)):
        print("suspicion of influenza")
    elif weakness and (not fever and not musclePain):
        print("jus take a break")
    else:
        print("you may be cold")

#6
    isCheckCompleted = False
    print("CHECKED IS COMPLITED" if isCheckCompleted else "CHECK NOT DONE YET")