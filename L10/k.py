class SimpleList:
    def __init__(self):
        self._list = []

    def __getitem__(self, key):
        return self._list[key] if -1<key< len(self._list) else None
    
    # def __setitem__(self, key, value):
    #     if value >= 0 and not key in self._list.keys():
    #         self._list[key] = value

    def append(self, value):
        if value >= 0:
            self._list.append(value)

if __name__ == '__main__':
    d = SimpleList()
    d.append(1)
    d.append(2)
    d.append(-4)
    d.append(3)
    d.append(4)
    print(d[0])
    print(d[1])
    print(d[2])
    print(d[3])
    print(d[5])
    print(d[-1])