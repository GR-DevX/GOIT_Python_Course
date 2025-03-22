#Декоратори

import time
def decorator(func):

    def inner_function(*args,**kwargs):
        print(f'Функція: {func.__name__} з параметрами: {args}, {kwargs}')

        result=func(*args,**kwargs)

        print(f"Результат: {result}")
        return result

    return inner_function

def decorator2(func):

    def inner_function(*args,**kwargs):
        print("dec 2 started")
        t=time.time()

        result=func(*args,**kwargs)

        print(f"time taken: {time.time()-t}")
        print("dec 2 ended ")
        return result

    return inner_function


@decorator
@decorator2
def add(x:int,y:int)->int:
    return x+y

@decorator
def mult3(a,b,c):
    return a*b*c
if __name__=='__main__':
    #add=decorator(add)
    print(add(1,2))
    print()
    print(mult3(1,2,4))