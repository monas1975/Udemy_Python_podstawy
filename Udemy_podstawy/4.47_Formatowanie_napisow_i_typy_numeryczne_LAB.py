if __name__ == '__main__':

#1. Zadeklaruj zmienną name i przypisz do niej swoje imie
 name ='Tomek'

#2. Zadeklaruj zmienną age i przypisz do niej wiek

 age =46

#3. Zadeklaruj zmienną daysInYear i przypisz jej wartość 365
 daysInYear =365

#4. Zadeklaruj zmienną message i przypisz jej wartość jak poniżej.
# Uwaga w miejscu ??? należy umieścić znaczniki pozwalające
# na wyświetlenie kolejno napisu i dwóch liczb

 message = name + ' is ' + str(46) + ' so is about ' + str(46*daysInYear) + ' days old'
 message2 = '%s is %d years old, so is about %d days old'

# 5. Wyświetl informację jak poniżej (wykorzystaj funkcje formatowania napisów)j:

 print(message)
 print(message2 % (name,age,age*daysInYear))

#6. Zmień imie i wiek w zmiennych name i age i
# jeszcze raz wyświetl komunikat korzystając z tej samej instrukcj co poprzednio
 name = 'Anka'
 age =45

 print(message2 % (name,age,age*daysInYear))

 message ='%s is %d years old, so it is about %d days old'

#7. Zmień wartość zmiennej message na:

 message3 = '{0:s} is {1:d} years old, so is about {2:d} days old...'


#8. Stosując metodę format dla zmiennej message wyświetl komunikat w postaci:
 print(message3.format(name,age,age*daysInYear))

#9. Wyznacz wynik dzielenia całkowitego i resztę z dzielenia 1234567890 przez 12345:
 result1 = 1234567890 // 12345 #dzielenie calkowite
 result2 = 1234567890 % 12345 # reszta z dzielenia

 message4 = '1234567890 divided by 12345 is {0:d} and the rest is {1:d}'

 print(message4.format(result1, result2))

