from collections import namedtuple
t1=(2,3)
t2=(3,4)
# h1=('John','Doe',35,'j.doe@mail.com','+123456789')
Dot=namedtuple('Точка',['x','y'])
p1=Dot(x=3,y=6)
p2=Dot(y=4,x=2)
print(p1)
print(p2)
print(isinstance(p1,Dot),isinstance(p2,Dot))
# ERROR!!!!!
# p1.y=5
print(f"p1.x={p1.x}, p1.y={p1.y}")
print(t1,t2)
