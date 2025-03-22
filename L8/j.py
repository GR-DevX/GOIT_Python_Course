#map
numbers=[i for i in range(1,11)]
print(numbers)

numbers=list(map(lambda x:x*x,numbers))
print(numbers)

def f(n):
    return '0'+str(n)
print(list(map(f,range(1,11))))
# 1,2,3,4,5,6,7,8,9,10
# 1,2,3,4,5
print(list(map(lambda x,y:x+y,range(1,11),range(31,36))))
print([x+y for x,y in zip(range(1,11),range(1,6))])
