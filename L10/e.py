class CountDown:
    def __init__(self, n):
        self.n = n
        self.start = n

    def __iter__(self): # важливо тут
        return self
    
    def getState(self):
        return self.n
    
    def reset(self):
        self.n = self.start

    def setState(self, n):
        self.n = n if n < self.start and n>0 else self.n

    def __next__(self): # важливо тут
        if self.n == 0:
            raise StopIteration #зупинка генерації
        self.n -= 1
        return self.n
    
if __name__ == '__main__':
    cd=CountDown(50)
    for i in range(5):
        print(next(cd))
    print(f'State: {cd.getState()}')
    cd.reset()
    print(f'State: {cd.getState()}')
    for i in range(5):
        print(next(cd))
    print(f'State: {cd.getState()}')
    next(cd)
    next(cd)
    next(cd)
    print(f'State: {cd.getState()}')
    cd.setState(10)
    print(f'State: {cd.getState()}')
    cd.setState(100)
    print(f'State: {cd.getState()}')