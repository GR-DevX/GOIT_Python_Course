class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32 
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls((fahrenheit - 32) * 5 / 9)
    
if __name__ == '__main__':
    t = Temperature(20)
    print(t.celsius)
    t2=Temperature.from_fahrenheit(68)
    print(t2.celsius)
    print(Temperature.celsius_to_fahrenheit(t.celsius))