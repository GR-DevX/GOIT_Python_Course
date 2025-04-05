import json

# class SneakDict(dict):
#     def __repr__(self):
#         return('Nope))')
#     def get_num(self):
#         if self['num'] is not None:
#             return self["num"]

some_data={
    "key":"value",
    2:[1,2,3],
    'num':4,
    'my tuple':(5,6),
    'mydict':{'dkey':'dvalue'},
    True:True,
    None:None,
    'ключ':'значення',
}

# a=SneakDict(some_data)
with open('data0.json','w') as f:
    json.dump(some_data,f)
# print(a)
# print(repr(a))
# with open('data1.json','w') as f:
#     json.dump(a,f)
