if __name__ == '__main__':
#1. Pracujesz w Urzędzie Stanu Cywilnego i ...
# korzystasz z Pythona. Dziewczyna o imieniu Kasia i nazwisku Sowa
# wychodzi za mąż za chłopaka o nazwisku Mrugała.
# Pani Kasia chce zachować oba nazwiska.

#Zdefiniuj zmienne firstName, famillyName i lastName i
# przypisz do nich napisy odpowiadające imieniu, nazwisku panieńskim i
# nowym nazwisku. Następnie utwórz zmienną newName i zapisz
# w niej wynik konkatenacji (czyli złączenia napisów) dla firstname,
# spacji, familyName, spacji i lastName. Wyświetl to nowe nazwisko

 firstName = "Katarzyna"
 familyName = "Sowa"
 lastName = "Mrugala"

 newName = firstName + " " + familyName + " " + lastName
 print(newName)


#2. Zdefiniuj zmienną music o następującej zawartości (są to tytuły i autorzy piosenek z filmu Minionki):

#"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I'm a Man" Steve Winwood

#Uwaga! Ten napis zawiera zarówno apostrof jak i cudzysłów, więc musisz zmodyfikować zapis metodami pokazanymi na tej lekcji, żeby zdefiniowanie zmiennej się udało.

 music = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'
 print(music)



#3. W powyższym tekście mowa jest o 3 piosenkach.
# Zmień tekst tak, aby druga i trzecia piosenka podczas wyswietlania
# były umieszczone w nowej linii (znowu musisz w tekście dodać pewne
# znaki specjalne prezentowane na lekcji).
 music = '"Universal Fanfare" Jerry Goldsmith \n "Happy Together" Garry Bonner \n "I\'m a Man" Steve Winwood'
 print(music)

#4. Przygotuj kilka poleceń print, które wyświetlą taki oto ascii art
# :

# (\( \
#     ( -.-)
# O_(")(")


 a = '(\\( \\ \n    ( -.-) \n 0_(")(")'


 print(a)