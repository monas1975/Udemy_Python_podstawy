if __name__ == '__main__':
    isAutomaticMode = True
    is80PercentLight = True
    isDirectLight = False
    isRainy = False

    turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
    print(isAutomaticMode)
