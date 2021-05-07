if __name__ == '__main__':
    print('-------------')
    #1. Utwórz obiekt dictionary o
    # nazwie chanels z następującymi kluczami i wartościami:
    #-Google - 1480
    #-Email - 300
    #-Natural Traffic - 440
    #-TV Spot - 700

    chanels = {'Google':1480,'Email':300,'Natural Traffic':440,'TV Spot':700}
    print(chanels)

    #2. Wyświetl wartość skojarzoną z kluczem "Email"
    print(chanels['Email'])

    #3. Utwórz nowy słownik chanelsUpdate z kluczami i
    # wartościami:
    # -Natural Traffic -  520
    # -News - 600

    chanelsUpdate = {'Natural Traffic':520, 'News':600}

#4.Zaktualizuj słownik chanels wartościami z chanelsUpdate
    chanels.update(chanelsUpdate)
    print(chanels)

#5. Wyświetl wszystkie klucze z chanels
    print(chanels.keys())

#6. Usuń wartość 'Email' ze słownika
    print('---------------------')
    print(chanels)
    chanels.pop('Email')

    print(chanels)



