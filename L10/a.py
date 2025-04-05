from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int
    # def __post_init__(self):
    #     if self.width < 0:
    #         raise ValueError(f'Width {self.width} is not positive')
    #     if self.height < 0:
    #         raise ValueError(f'Height {self.height} is not positive')

    @property
    def area(self):
        return self.width * self.height
    
# @dataclass
# class Human:
#     name: str
#     last_name: str
#     age: int
#     phone: str
#     email: str
#     address: str



if __name__ == '__main__':
    r = Rectangle(10, 20)
    print(r.area)
    r2=Rectangle(5, 10)
    print(r2.area)
    print(f"r1: {r}")
    print(f"r2: {r2}")
