# pickle - серіалізація через byte string
import pickle

class A:
    def __init__(self,n:int):
        self.n=n
    
    def foo(self,a,b):
        return (a+b,self.n)

# expenses={'hotel':150,'breakfast':30,"taxi":15,"lunch":20,'test':'test'}

# serialized=pickle.dumps(expenses)
a=A(10)
serialized=pickle.dumps(a)
print(serialized)
print(type(serialized))
deserialized=pickle.loads(serialized)
print(deserialized)
print(type(deserialized))
print(deserialized.foo(2,3))