class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def change_factor(self, factor):
        self.factor = factor

    def __call__(self, x):
        return self.factor * x
    
class Counter:
    def __init__(self):
        self.count = 0

    def getCounter(self):
        return self.count 

    def __call__(self):
        self.count += 1
        return self.count

if __name__ == '__main__':
    double = Multiplier(2) # __init__
    #triple = Multiplier(3)
    print(double(5)) # __call__
    print(double(10)) # __call__
    double.change_factor(3) # change_factor
    print(double(20)) # __call__
    print(double(4)) # __call__
    #print(triple(5))

    counter=Counter() # __init__
    counter() # __call__
    counter() # __call__
    print(f"Counter called {counter.getCounter()} times")