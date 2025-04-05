# Серіалізація
expenses={'hotel':150,'breakfast':30,"taxi":15,"lunch":20,'test':'test'}
print(expenses)
print(type(expenses))

def serialize(d:dict)->str:
    l=[]
    for k in d:
        l.append(f"{k}:{d[k]}")
    return '|'.join(l)

def deserialize(s:str)->dict:
    l=s.split('|')
    # ['hotel:150' 'breakfast:30' 'taxi:15' 'lunch:20' 'test:test']
    d={}
    # [ ['hotel' '150'] ['breakfast' '30'] ['taxi' '15'] ['lunch' '20'] ['test' 'test'] ]
    for el in l:
        k,v=el.split(':') # Розпаковуємо список, завідомо маємо 2 значення
        if v.isdigit():
            v=int(v)
        d[k]=v
    return d

serialized=serialize(expenses)
print(serialized)
print(type(serialized))

deserialized=deserialize(serialized)
print(deserialized)
print(type(deserialized))