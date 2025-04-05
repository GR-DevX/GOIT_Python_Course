# JSON - Java Script Object Notation через  string
import json

some_data={
    "key":"value",
    2:[1,2,3],
    'num':4,
    'my tuple':(5,6),
    'mydict':{'dkey':'dvalue'},
    True:True,
    None:None,
}

json_string=json.dumps(some_data)
print(json_string)
print(type(json_string))

print()
restored_data=json.loads(json_string)
print(restored_data)
print(type(restored_data))