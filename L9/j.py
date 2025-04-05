# Абстракція 1
from typing import Protocol

class Animal(): #інтерфейс
    def speak(self)->str:
        pass

class Dog:
    def speak(self)->str:
        return 'woof'
    def walk(self):
        pass

class Bird:
    def speak(self)->str:
        return 'tweet'
    def fly(self):
        pass

class Fish:
    def speak(self)->str:
        return 'bulk'
    def swim(self):
        pass


if __name__=='__main__':

    def say_something(speaker:Animal):
        print(speaker.speak())

    d=Dog()
    b=Bird()
    f=Fish()

    say_something(f)
    say_something(b)
    say_something(d)