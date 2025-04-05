# Інкапсуляція
class Person:
    def __init__(self,name:str,age,money:float=0):
        self.name=name.capitalize()
        self._age=int(age) # Protected 
        self.__money=float(money) # Private

    @property
    def money(self): # getter 
        return self.__money
    
    @money.setter
    def money(self,amount): #setter
        self.__money=float(amount)

    def greeting(self)->str:
        return f"Hi {self.name}"
    
if __name__=='__main__':
    p=Person('остап','23',200_000.00)
    # print(dir(p))
    #print(p.__money)
    print(p.name)
    p.money='2000'
    print(p.money)
    p.money*=3
    print(p.money)