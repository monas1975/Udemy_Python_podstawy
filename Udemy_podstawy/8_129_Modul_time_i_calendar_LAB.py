import time
import calendar
if __name__ == '__main__':
    print(time.time()) #unix
    print(time.asctime(time.localtime()))

    print(calendar.month(1975,1))
    calendar.setfirstweekday(6)
    print(calendar.month(1975, 1))

    print(calendar.isleap(2000))

    print(calendar.month(2021,12))
