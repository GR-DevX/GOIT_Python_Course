# Наслідування (успадковування)

class Animal: # батьківський
    def __init__(self,word='', name=''):
        self.word=word
        self.name=name
    
    def say(self):
        print(f'{self.name} says {self.word}')

class Cat(Animal): # дочірній
    def __init__(self,name=''):
        self.name=name
        self.word='meow'

class Dog(Animal): # дочірній
    def __init__(self,name=''):
        self.name=name
        self.word='woof'


if __name__=='__main__':
    an1=Dog('Sirko')
    an2=Cat('Zhmuryk')
    an3=Cat('Tovstun')

    an2.say()
    an3.say()
    an1.say()