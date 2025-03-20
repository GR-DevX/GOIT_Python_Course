from collections import namedtuple
t1=(2,3)
t2=(3,4)
Human=namedtuple('Human',['name','lname','age','email','phone'])
h1=Human('John','Doe',age=35,phone='+123465798',email='j.doe@mail.com')
# h1=('John','Doe',35,email='j.doe@mail.com',phone='+123465798')
Dot=namedtuple('Точка',['x','y'])
p1=Dot(x=3,y=6)
p2=Dot(y=4,x=2)
p3=Dot(5,y=[1,2])

p3.y[0]=5
print(p1)
print(p2)
print(p3)

print(isinstance(p1,Dot),isinstance(p2,Dot))
# ERROR!!!!!!!
# p1.y=5
print(f"p1.x={p1.x}, p1.y={p1.y}")
print(t1,t2)

print(f"There is a guy named {h1.name} {h1.lname} who is age of {h1.age} and his contacts are:\nemail:\
{h1.email}\nphone:{h1.phone}")
print(h1)