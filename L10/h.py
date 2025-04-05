class SimpleContextManager:
    def __init__(self, n):
        self.n = n
    
    def __enter__(self):
        print('Entering the context')
        return self.n
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f'Exiting the context with value:{self.n}')
        return True
    
if __name__ == '__main__':
    counter=SimpleContextManager(10)
    with counter as c: #__enter__, c=counter.n
        c*=2
        print(f'c={c}')
        counter.n=100
        c*=2
        print(f'c={c}')
        # __exit__
    with counter as c: #__enter__, c=counter.n
        print(c)
        #__exit__
    print(f'Value of counter: {counter.n}')
    