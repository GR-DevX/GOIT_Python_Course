#zip
print(list(map(lambda x:x[0]*x[1],zip(range(31,36),range(1,6)))))
s='some text'
print(list(map(lambda x:f"{x[1]}:{x[0]}", zip(s,range(len(s))))))
print(list(zip(s,range(len(s)))))

print([x+y for x,y in zip(range(11),range(10,21))])
print(list(map(lambda x,y:x+y,range(1,11),range(10,21))))

