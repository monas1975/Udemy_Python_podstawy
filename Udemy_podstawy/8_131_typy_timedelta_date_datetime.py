import datetime


if __name__ == '__main__':
    print(datetime.MINYEAR, datetime.MAXYEAR)

    print(datetime.timedelta(days=-1))
    print(datetime.timedelta(hours=-1))
    print(datetime.timedelta(minutes=-30))

    d1 = datetime.timedelta(days=1, hours=2, minutes=-30)
    print(d1)
    d2 = datetime.timedelta(days=-1, hours=2-2, minutes=-3)
    print(d2)

    print(d1+d2)
    print('-------------------------------------')

    print(datetime.date.today())
    today = datetime.date.today()
    daysToPay = datetime.timedelta(days=7)
    print('today is',today)
    print('rachunek do zapplaty:',today+daysToPay)
    print('-------------------------------------')

    endOfTheWorld = datetime.date.max
    print(endOfTheWorld)
    print(endOfTheWorld.weekday())

    bornDate = datetime.date(1975,1,3)
    print(today-bornDate)
    bornDate2 = datetime.date(1976, 10, 3)
    print(today - bornDate2)

    print('=================================')
    print(datetime.datetime.now())
    print(datetime.datetime.today())
    print(datetime.datetime.utcnow())
    print(datetime.datetime.today().weekday())

    print("%a",datetime.datetime.now().strftime("%a"))
    print("%A", datetime.datetime.now().strftime("%A"))
    print("%w", datetime.datetime.now().strftime("%w"))
    print("%a %A %w", datetime.datetime.now().strftime("%a %A %w"))

    print("%Y-%m-%d_%H_%M%S_%f",\
          datetime.datetime.now().strftime("%Y-%m-%d_%H_%M%S_%f"))
