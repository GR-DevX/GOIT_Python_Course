from dataclasses import dataclass

@dataclass
class RecCub: # rectangular cuboid
    width: float
    height: float
    depth: float
    
    def __post_init__(self):
        if self.width < 0:
            raise ValueError(f'Width {self.width} is not positive')
        if self.height < 0:
            raise ValueError(f'Height {self.height} is not positive')
        if self.depth < 0:
            raise ValueError(f'Depth {self.depth} is not positive')

    @property
    def volume(self)->float:
        return self.width * self.height * self.depth
    
    @property
    def area(self):
        return 2*(self.width*self.height+self.width*self.depth+self.height*self.depth)
    
    def __eq__(self, other):
        return self.volume == other.volume \
                                if isinstance(other, RecCub) \
                                else self.volume == float(other)
    
    def __lt__(self, other):
        return self.volume < other.volume if isinstance(other, RecCub) else self.volume < other
    
    def __gt__(self, other):
        return self.volume > other.volume if isinstance(other, RecCub) else self.volume > other
    
    def __le__(self, other):
        return self.volume <= other.volume if isinstance(other, RecCub) else self.volume <= other
    
    def __ge__(self, other):
        return self.volume >= other.volume if isinstance(other, RecCub) else self.volume >= other
    
    def __ne__(self, other):
        return self.volume != other.volume if isinstance(other, RecCub) else self.volume != other
    
    def __repr__(self):
        return f'RecCub(width={self.width}, height={self.height}, depth={self.depth})' 
    
    def __str__(self):
        return f"Rectangular cuboid with dimensions "\
        f"{self.width}x{self.height}x{self.depth}:\n"\
        f"Volume: {self.volume}\n"\
        f"Area: {self.area}"
    
if __name__ == '__main__':
    a=RecCub(1,2,3)
    b=RecCub(2,3,4)
    print(a)
    print(b)
    print(a<b) # __lt__
    print(a>=10.5) # __ge__
    print(a=='6') # __eq__
    if  a<10.0:
        print('Good))')
    