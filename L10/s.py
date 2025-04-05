class Car:
    tax = 0.1

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    @property
    def final_price(self):
        return self.price + self.price * self.tax
    
    @classmethod
    def set_tax(cls, tax):
        cls.tax = tax

if __name__ == '__main__':
    car1=Car('Ferrari','F40',1000)
    print(f"Final price: {car1.final_price}")
    Car.set_tax(0.2) # тут змінили класову змінну tax
    car2=Car('Nissan','Silvia',2000)
    print(f"Final price car2: {car2.final_price}")
    print(f"Final price car1: {car1.final_price}")
