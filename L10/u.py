class Animal:
    def __init__(self,name,breed):
            self.name=name
            self.breed=breed

    @classmethod
    def create(cls, species):
        species_map = {
            'dog': cls.Dog,
            'cat': cls.Cat
        }
        return species_map.get(species,Animal)('Default_name')

    class Dog():
        def __init__(self,name,*args):
            self.name=name
        def speak(self):
            return "Woof"
    
    class Cat():
        def __init__(self,name):
            self.name=name
        def speak(self):
            return "Meow"
    
if __name__ == '__main__':
    an1=Animal.create('dog')
    an2=Animal.create('cat')
    an3=Animal.create('elephant')
    print(an1.speak())
    print(an2.speak())
    print(an1.__class__)
    print(an2.__class__)
    print(an3.__class__)
    print(an1.name)