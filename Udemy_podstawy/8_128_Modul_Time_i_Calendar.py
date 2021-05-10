
import time
import calendar
if __name__ == '__main__':

    print("Curent time, unix epoch", time.time())
    print("\n")
    print("current time is... tuple",time.localtime(time.time()))
    print("\n")
    print("current time is.... for human", time.asctime(time.localtime(time.time())))
    print("\n")
    print('-------')
  #  print("current time is.... for human",time.localtime(time.clock()))

    print('+++++++  calendar')
    print(calendar.month(2020,9,w=1,l=2))
    print("\n")
    print(calendar.month(2021, 5))
    print("\n")
    print('week day is',calendar.weekday(2021,5,10))
    calendar.setfirstweekday(6)
    print(calendar.month(2021, 5))
    print('week day is', calendar.weekday(2021, 5, 10))
    print("\n")
    print('is 2020 a leap year',calendar.isleap(2020))
    print("\n")
    print('Leap days 2000 - 2017',calendar.leapdays(2000,2017))
    print('Leap days 2000 - 2020', calendar.leapdays(2000, 2017))
    print('Leap days 2000 - 2017', calendar.leapdays(2000, 2021))

    print(calendar.calendar(2021))

