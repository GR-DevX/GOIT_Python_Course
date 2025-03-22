#filter
f=filter(lambda x:x%2==1,range(1,11))
print(list(f))

def g(x):
    return x>'l'
f=filter(g,'hello world')
print(set(f))

d={0:1,2:3,3:4}
f=filter(lambda x:x[0]>1,d.items())
print(dict(f))
f=filter(lambda x:x[0]>1,d.items())
print(list(f))