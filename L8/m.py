#reduce
from functools import reduce

def add(x,y):
    print(f"x={x}, y={y}")
    return x+y
res=reduce(add,range(1,7))
print(res)