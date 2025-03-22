# функція у колекції (трохи карінг та замикання)

from typing import Callable

def add(a:int,b:int) -> int:
    return a+b

def multiply(a:int,b:int) -> int:
    return a*b

def power(b:int) -> int:
    def inner_power(a:int):
        return a**b # return a**2
    return inner_power

def apply_operation(a:int, b:int, op:Callable[[int,int],int]) ->int:
    return op(a,b)

operations={
    'add':add,
    'mult':multiply,
    'pow':power,
    'square':power(2),
    'qube':power(3),
}

if __name__=='__main__':
    print(operations['add'](3,5))
    print(operations['mult'](3,5))
    print(operations['pow'](3)(5))
    print(operations['square'](5))
    print(operations['qube'](5))