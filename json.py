import json

data = {"name": "Ali", "age": 17, "city": "Almaty"}

json_data = json.dumps(data)
print(json_data)       # {"name": "Ali", "age": 17, "city": "Almaty"}
print(type(json_data)) # <class 'str'>



import json

json_data = '{"name": "Ali", "age": 17, "city": "Almaty"}'
data = json.loads(json_data)

print(data)       # {'name': 'Ali', 'age': 17, 'city': 'Almaty'}
print(type(data)) # <class 'dict'>


import json

data = {"name": "Dana", "age": 18}

with open("data.json", "w") as f:
    json.dump(data, f)  # writes JSON to file



import json

data = ["apple", "banana", "cherry"]
json_data = json.dumps(data)
print(json_data)       # ["apple", "banana", "cherry"]
print(type(json_data)) # <class 'str'>

py_list = json.loads(json_data)
print(py_list)         # ['apple', 'banana', 'cherry']



import json

with open("data.json", "r") as f:
    data = json.load(f)  # reads JSON from file

print(data)  # {'name': 'Dana', 'age': 18}