def mul2(m:int)->int|None:
    if isinstance(m,int):
        n=m
        if n<0:
            n=-n
        n=n*2
        return n
    else:
        return None
    

a=-3
b=4
mul2()
print(mul2(a))
print(mul2(b))
print(mul2('3'))
