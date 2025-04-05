from enum import Enum,auto

class Day(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()

# class.VALUE = (n p/p)
class LogLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    #WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()
    FATAL = auto()

def f():
    pass

class LogLevelHandMade(Enum):
    DEBUG = '1'
    INFO = '2'
    WARNING = '3'
    ERROR = f
    CRITICAL = '5'
    FATAL = lambda x: x+1

def setLogLevel(self,level):
    pass

class Color(Enum):
    RED=auto()
    GREEN=auto()
    BLUE=auto()
    WHITE=auto()
    BLACK=auto()
    YELLOW=auto()



if __name__=='__main__':
    # print(Day.MONDAY)
    # print(Day.MONDAY.name)
    # print(Day.MONDAY.value)
    # today=Day.THURSDAY
    # print(today)
    # print(today==Day.THURSDAY)
    # print(today.value==4)
    for i in range(len(LogLevel)):
        print(f"{LogLevel(i+1)} : {LogLevel(i+1).value}")
    print(LogLevelHandMade.FATAL(1))

    # setLogLevel(LogLevel.DEBUG)
    # setColor(Color.RED) setColor(colors['RED'])