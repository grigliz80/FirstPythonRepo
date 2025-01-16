import json

with open('db/cj.json') as file_obj:
    cj = json.load(file_obj)


for k, v in cj.items():
    print(k, ':', v)