if __name__ == '__main__':
    CountryLeaders={'PL':'Duda','US':'Trump'}
    print(CountryLeaders)
    print(CountryLeaders['US'])
    print(CountryLeaders['PL'])

    CountryLeaders['DE'] = 'Merkel'
    print(CountryLeaders)

    print(CountryLeaders.keys())
    print(CountryLeaders.items())
    print(CountryLeaders.values())
    print('----------------------')
   # print(CountryLeaders.popitem())
    print(CountryLeaders)
    print('----------------------')
    print(CountryLeaders.setdefault('FR','Macron'))
    print(CountryLeaders)

    print(CountryLeaders.get('PL'))
    print(CountryLeaders.get('RU'))

    print('----------------------')

    NewLeaders = {'RU':'Putin','DE':'Schultz'}
    print(CountryLeaders)
    CountryLeaders.update(NewLeaders)
    print(CountryLeaders)

