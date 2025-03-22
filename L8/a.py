# функція як значення змінної
from typing import Callable

def add(a:int,b:int) -> int:
    return a+b

def multiply(a:int,b:int) -> int:
    return a*b

def apply_operation(a:int, b:int, op:Callable[[int,int],int]) ->int:
    return op(a,b)

if __name__=='__main__':
    result_add=apply_operation(4,5,add)
    result_multiply = apply_operation(3,5,multiply)
    print(result_add,result_multiply)