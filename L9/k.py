# Абстракція 2
from abc import ABC,abstractmethod

class Animal(ABC): # абстрактний клас
    @abstractmethod
    def speak(self)->str:
        pass
    

class Dog(Animal):
    def speak(self)->str:
        return 'woof'
    def walk(self):
        pass

class Bird(Animal):
    def speak(self)->str:
        return 'tweet'
    def fly(self):
        pass

class Fish(Animal):
    def speak(self)->str:
        return 'bulk'
    def swim(self):
        pass


if __name__=='__main__':

    d=Dog()
    b=Bird()
    f=Fish()
    a=Animal()
    def say_something(speaker:Animal):
        print(speaker.speak())
    for i in [d,b,f,a]:
        say_something(i)

