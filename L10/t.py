class Animal:
    @classmethod
    def create(cls, species):
        species_map = {
            'dog': Dog,
            'cat': Cat
        }
        return species_map.get(species,Animal)()

class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
if __name__ == '__main__':
    an1=Animal.create('dog')
    an2=Animal.create('cat')
    print(an1.speak())
    print(an2.speak())
    print(an1.__class__)
    print(an2.__class__)