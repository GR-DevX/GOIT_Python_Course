class StrangeClass:
    def __init__(self):
        pass
    def __getitem__(self, key:int):
        return lambda x: x**key
    def __call__(self, key:int):
        return lambda x: x**key
if __name__ == '__main__':
    sc=StrangeClass()
    double=sc[2]
    triple=sc[3]
    # print(double(5))
    # print(triple(5))
    l=[sc[i] for i in range(2,6)]
    m=[sc(i) for i in range(2,6)]
    for f in m:
        print(f(5))