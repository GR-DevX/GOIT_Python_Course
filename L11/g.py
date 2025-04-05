import json
# class SneakDict(dict):
#     def __repr__(self):
#         return('Nope))')
#     def get_num(self):
#         if self['num'] is not None:
#             return self["num"]

with open('data0.json','r',encoding='utf-8') as f:
    data=json.load(f)
#data=SneakDict(data)
print(data)
print(type(data))