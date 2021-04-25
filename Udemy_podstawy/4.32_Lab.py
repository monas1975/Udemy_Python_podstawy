if __name__ == '__main__':
#1. Wyświetl napisy: TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV. Użyj jednego polecenia print
    print('TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV')

#2. Wyświetl w/w teksty używając jako separatora znaku ";"

print('TVP1', 'TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV', sep=';')

#3. Korzystając z jednego polecenia print wyświetl
# napis (bez podtekstów!):
#I like computers but better is TVP1 but better
# is TVP2 but better is TVN but better is Polsat
# but better is BBC but better is HBO but better
# is MTV

print('I like computers but better is TVP1 but better is TVP2 but better is TVN but better is Polsat but better is BBC but better is HBO but better is MTV')

#4. Zadeklaruj zmienne ProgramName o wartości
# 'BBC', Item o wartości 'News'' i
# Time o wartości '18:00'.

ProgramName='BBC'
Item = 'News'
Time = '18:00'

print('I like watching ',Item, ' at ',Time, ' on ',ProgramName,'.')