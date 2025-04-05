from collections import UserDict
class MyDict(UserDict):
    def __add__(self, other):
        temp_dict=self.data.copy()
        temp_dict.update(other.data)
        return MyDict(temp_dict)
    
    def __sub__(self, other):
        temp_dict=self.data.copy()
        for key in other.data.keys():
            if key in temp_dict.keys():
                temp_dict.pop(key)
        return MyDict(temp_dict)
    
if __name__ == '__main__':
    d1 = MyDict({'a': 1, 'b': 2})
    d2 = MyDict({'c': 3, 'd': 4})
    d3 = d1 + d2
    print(d3.data)
    d4 = d3 - d2
    print(d4.data)
    d5 = d3 - d1
    print(d5.data)