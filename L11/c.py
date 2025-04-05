# pickle - серіалізація через файл
import pickle

class A:
    def __init__(self,n,m:int):
        self.n=n
    
    def foo(self,a,b):
        return (a+b,self.n)


# expenses={'hotel':150,'breakfast':30,"taxi":15,"lunch":20,'test':'test'

# with open('data0.pickle','wb') as f:
#     pickle.dump(expenses,f)

# with open('data0.pickle','rb') as f:
#     deserialized=pickle.load(f)

# print(deserialized)
# print(type(deserialized))

# a=A(10)
# with open('data1.pickle','wb') as f:
#     pickle.dump(a,f)
with open('data1.pickle','rb') as f:
    b=pickle.load(f)

print(b)
print(b.foo(6,1))