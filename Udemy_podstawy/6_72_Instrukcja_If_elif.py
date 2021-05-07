if __name__ == '__main__':
    age = 27
    isDrunk = False
    isRestrictedAre = True

    print("gorsza metoda")

    if age < 18:
        print("jestes za mlody")
    else:
        if isDrunk:
            print("jestes pijany")
        else:
            if isRestrictedAre:
                print("tutaj nie mozna pic")
            else:
                print("mozesz kupic alkohol")

    print('------------')
    print('lepsza')

    if age >= 18 and not isDrunk and not isRestrictedAre:
        print('mozesz kupic browaca')
    elif age < 18:
        print('za mlody')
    elif isDrunk:
        print("jestes pijany")
    elif isRestrictedAre:
        print("tu nie mozna pic")