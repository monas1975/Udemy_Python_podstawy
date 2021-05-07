if __name__ == '__main__':
    age = 27

    if age >=18:
        print("you are adult and you can buy alcohol")
    else:
        print("you are too young to buy alcohol")

    isDrunk = False

    if age >=18 and not isDrunk:
        print("you are adult and you can buy alcohol")
    else:
        print("we cann't swll you alcohol")

    isRestrictedArea = False

    if age >=18 and not isDrunk and not isRestrictedArea:
        print("you are adult and you can buy alcohol")
    else:
        print("we cann't swll you alcohol")