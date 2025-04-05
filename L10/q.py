class Car:
    def __init__(self,model,year):
        self.model=model
        self.year=year

    def __repr__(self):
        return f'Car(model={self.model}, year={self.year})'
    
    @staticmethod
    def is_classic(year):
        return year<2000
    
    @classmethod
    def from_string(cls, s):
        model,year=s.split(',')
        return cls(model, int(year))
    
if __name__ == '__main__':
    print(Car.is_classic(1999))
    print(Car.is_classic(2010))
    c=Car.from_string("Ferrari,1999")
    print(f"c={c}")
    c=Car('Mercedes', 2010)
    print(f"Model: {c.model}, Year: {c.year}")
    print(c.is_classic(c.year))