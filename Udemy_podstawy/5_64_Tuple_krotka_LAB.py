if __name__ == '__main__':
    #1. Utwórz listę o nazwie marketing z elementami:
#-loyality program
#-client promotion
#-market research
    marketing =['loyality program','client promotion','market research']
    print(marketing)

#2. Dodaj do listy element 'public relations'
    marketing.append('public relation')
    print(marketing)

#3. Wyświetl pozycję numer 3
    print(marketing[3])
#4. Wstaw na pozycję numer 2 element 'investor relations'
    marketing.insert(2,'investor relation')
    print(marketing)
#5. Chcesz jednak aby lista znajdowała się w zmiennej
# o nazwie emailMarketing. Skopiuj elementy z
# listy marketing do listy emailMarketing
    emailMarketing = marketing.copy()
    print(emailMarketing)
#6. Posortuj listę emailMarketing
    emailMarketing.sort()
    print(emailMarketing)
#7. Utwórz nową jednoelementową listę internalEmails.
# Jedyny element to 'internal communication'
    internalEmails =['internal communication']
#8. Dodaj listę internalEmails do listy emailMarketing
    print('------------------------------')
    emailMarketing.extend(internalEmails)
    print(emailMarketing)
#9. Utwórz tuple, którego wartości pochodzą z
# listy emailMarketing. Podczas wyświetlania
# tuple zwróć uwagę na nawiasy, z jakich skorzystał Python
    emailMarketingTuple = tuple(emailMarketing)
    print(emailMarketingTuple)
