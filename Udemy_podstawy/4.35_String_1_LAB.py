if __name__ == '__main__':

 # 1 Utwórz zmienną quote i
# przypisz jej następującą wartość:
# 'A good programmer is someone who always looks both ways before
# crossing a one-way street'
 quote = "A good programmer is someone who always looks both ways before crossing a one-way street"
# 2 Wyświetl tekst napisany tylko wielkimi literami

 print(quote.upper())

 # 3 Wyświetl tekst zapisany tylko małymi literami

 print(quote.lower())

# 4 Sprawdź czy tekst kończy się słowem 'street'

 print(quote.endswith('street'))

 # 5 Sprawdź czy tekst jest zapisany wielkimi literami

 print(quote.isupper())

 # 6 Sprawdź, czy tekst skonwertowany do wielkich liter jest
 # zapisany wielkimi literami (Zastosuj złożenie funkcji)

 print(quote.upper().isupper())

 # 7 Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo 'one'

 print(quote.find('one'))

 # 8 Zamień w tekście słowo 'one' na '1'

 print(quote.replace('one', '1'))

 # 9 Zamień w tekście słowo 'one' na '1' a słowo 'both' na 2

 print(quote.replace('one', '1').replace('both','2'))

 # 10 Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja

 print(quote.split(' '))

 # 11 Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi

 print(quote.isnumeric())
 print(quote.isdigit())
 print(quote.isalpha())
 print(quote.isalnum())

