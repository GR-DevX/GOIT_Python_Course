from dataclasses import dataclass
@dataclass
class Car():
    model:str
    make:str
    year:int
    engine:float
    fuel_type:str
    color:str

    def is_old(self):
        return self.year<1990
    
    def is_big_engine(self):
        return self.engine>3.0
