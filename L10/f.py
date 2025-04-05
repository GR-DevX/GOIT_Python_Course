import random
class RandIterator:
    def __init__(self,start,end,quantity):
        self.start=start
        self.end=end
        self.quantity=quantity
        self.count=0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.count+=1
        if self.count>self.quantity:
            raise StopIteration
        else:
            return random.randint(self.start,self.end)
        
if __name__ == '__main__':
    for i in RandIterator(1,10,20):
        print(i, end=' ')
    #here