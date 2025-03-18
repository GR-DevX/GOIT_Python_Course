def add(a,*args,b=8,**kwargs):
    sum=a
    # if 'b' in kwargs.keys():
    #     b=kwargs['b']
    # else:
    #     b=None
    for v in args:
        sum+=v
    print(args)
    print(kwargs)
    return sum,b

a,b=add(2,3,4,5,6,server="google.com", port=1033, version='1.1.2.1')
print(a,b)