import math
if __name__ == '__main__':

#1. Zaimportuj moduł math
#2 2. Oto wzory pozwalające na wykonanie konwersji stopni na radiany i radianów na stopnie:
#1° = (π * rad)/180
#1 rad = 180°/π

#3. Zadeklaruj zmienną degree i przypisz jej wartość 360.
# Wylicz i wyświetl ile wynosi wartość radianów dla 360 stopni
    degree = 360

    print(degree*math.pi/180)

#4. Zmień wartość zmiennej degree na 45 stopni i powtórz obliczenia
    degree = 45
    print(degree*math.pi/180)
    print('------------------------------')
#5. ... ale moduł math ma funkcję radians, która wykonuje konwersję
# stopni na radiany! Porównaj wyniki zwracane przez Twoje
# obliczenia z obliczeniami funkcji radians.

    print(math.radians(360))
    print(math.radians(45))

#6 6. Pizzeria oferuje pizze:
#small - promień 22 cm, cena, 11.50
#big - promień 27 cm, cena 15.60
#family - promień 38cm, cena 22.00
#Zadeklaruj zmienne small_pizza_r, big_pizza_r, family_pizza_r
# oraz small_pizza_price, big_pizza_price, family_pizza_price i
# zapisz w nich w/w wartości.

    small_pizza_r = 22
    big_pizza_r = 27
    family_pizza_r =38

#7. Oblicz pole powierzchni pizz w metrach kwadratowych
    small_pizza_P = math.pi*(math.pow(small_pizza_r/100,2))
    big_pizza_P = math.pi*(math.pow(big_pizza_r/100,2))
    family_pizza_P = math.pi*(math.pow(family_pizza_r/100,2))

    print(small_pizza_P)
    print(big_pizza_P)
    print(family_pizza_P)

# 8. Wyznacz cenę metra kwadratowego pizzy small, big i family
    small_pizza_Price = 11.50/small_pizza_P
    big_pizza_Price = 15.60/big_pizza_P
    family_pizza_Price = 22/family_pizza_P

    print(small_pizza_Price)
    print(big_pizza_Price)
    print(family_pizza_Price)

#9
    math_ls = dir(math)
    print(math_ls)