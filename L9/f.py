# множинне успадкування

class Animal:
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(f'{self.name} is walking as an animal...')

class Bird:
    def __init__(self,name):
        self.name=name
    def fly(self):
        print(f'{self.name} is flying...')
    def walk(self):
        print(f'{self.name} is walking as a bird...')


class Ship:
    def __init__(self,name):
        self.name=name
    def swim(self):
        print(f'{self.name} is swimming over the water...')

class Duck (Bird, Animal, Ship):
    pass

if __name__=='__main__':
    d1=Duck('Donald')
    d1.fly()
    d1.walk()
    d1.swim()
    print(Duck.mro())