# __ініт__
class Person: # клас
    call_counter=0
    def __init__(self,
                 name:str,
                 age,
                 email=None,
                 phone=''):
        self.name = name.capitalize()
        self.age = int(age)
        self.email = email
        self.phone = phone
        self.value=None
        

    def say(self):
        return f"hello, {self.name}"
    
    @staticmethod
    def increase_counter():
        Person.call_counter+=1

    def call(self):
        Person.increase_counter()
        return f"Calling {self.name} at {self.phone} (total calls: {Person.call_counter})"
    
    def mail(self):
        return f"Email to {self.email}"

p=Person('ostap',
         23,
         'ostap@mail.com',
         phone="+380688887766") #<- тут викликається __init__
# p - об’єкт
# р2 - теж об’єкт
p2=Person('pedro',65)#<- тут теж викликається __init__
print(p.call())
print(p.call())
print(p2.call())
print(p2.call())
print(p.call())
print(p.call())



#print(dir(p))
# print(p2.say())
# print(p2.call())
# p2.set_counter(100)
# print(p2.call())
# print(p2.mail())
# print()
# print(p2.say())
# print(p2.call())
# print(p2.call())
# print(p2.call())
# print(p2.call())
# print(p.call())
# print(p2.mail())
