# декоратор wraps
from functools import wraps

def decor(f):
    @wraps(f)
    def inner(*args,**kwargs):
        return f(*args,**kwargs)
    return inner

@decor
def sum(a,b):
    return a+b

if __name__=='__main__':
    print(sum(3,5))
    print(sum.__name__)