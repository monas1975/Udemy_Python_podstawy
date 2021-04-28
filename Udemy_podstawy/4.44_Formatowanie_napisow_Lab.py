if __name__ == '__main__':

# 1. Zadeklaruj zmienną helloMessage i wpisz do niej tekst:
#
# "Hello %s!"

 helloMessage = 'Hello %s!'

#2. Korzystając z tej zmiennej oraz z operatora % wyświetl
# dwa powitania:
#raz %s należy zamienić na Kate a raz na Chirs

 print(helloMessage % ('Kate'))
 print(helloMessage % ('Chris'))

#3. Zmień zawartość zmiennej helloMessage na

#"Hello {0:s}!"

 helloMessage = 'Hello {0:s} !'

#4. Podobnie , jak w punkcie drugim wyświetl powitanie
# z Kate i Chis, ale tym razem skorzystaj z metody format

 print(helloMessage.format('Kate'))
print(helloMessage.format('Chris'))

#5. Zmień zawartość zmiennej helloMessage na
#"%s has %d %s"

helloMessage = "%s has %d %s"

#6. Korzystając z tej zmiennej oraz z operatora % wyświetl dwa komunikaty.

#w pierwszym komunikacie %s zamień na Kate, %d na 1, a %s na animal

#w drugim komunikacie %s zamień na  Chris, %d na 100000, a %s na $

print(helloMessage % ('Kate',1, 'animal'))
print(helloMessage % ('Chris', 1000, '$'))

#7. Zmień zawartość zmiennej helloMessage na

#"{0:s} has {1:d} {2:s}"

helloMessage = "{0:s} has {1:d} {2:s}"

#8. Wyświetl te same komunikaty,
#jak w punkcie 6, ale tym razem skorzystaj z metody format
print(helloMessage.format('Kate',1,'animal'))
print(helloMessage.format('Chris',1000, '$'))

#9

line = "{0:20s} cost {1:6d} $"

print(line.format('ICE CREAM',3))

#10
line = "{0} {1:d}"

print(line.format("ICE CREAM",3))