class SimpleDict:
    def __init__(self):
        self._dict = {}

    def __getitem__(self, key):
        return self._dict[key] if key in self._dict.keys() else None
    
    def __setitem__(self, key, value):
        if value >= 0 and not key in self._dict.keys():
            self._dict[key] = value

if __name__ == '__main__':
    d = SimpleDict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = -4
    d['a'] = 3
    d['d'] = 4
    print(d['a'])
    print(d['b'])
    print(d['c'])
    print(d['d'])
   