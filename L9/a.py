# Класи
class Person:
    def __init__(self,name:str,age,email='',phone=''):
        self.name = name.capitalize()
        self.age = int(age)
        self.email = email
        self.phone = phone

    def say(self):
        return f"hello, {self.name}"
    
    def call(self):
        return f"Calling {self.name} at {self.phone}"
    
    def mail(self):
        return f"Email to {self.email}"

p=Person() #<- тут викликається __init__
p.name='ostap'
p.age=23
p.email='ostap@mail.com'
p.phone="+380688887766"
p2=Person()#<- тут теж викликається __init__
p2.name="Pedro"
print(p.say())
print(p2.say())