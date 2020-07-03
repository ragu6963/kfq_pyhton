import json

customer = {
    'id':15213,
    'name':'정우영',
    'history':[
        {'data':'2019-02-02','item':'iPhone'},
        {'data':'2020-02-02','item':'Monitor'},
    ]
}

jsonString = json.dumps(customer)
# print(jsonString)

with open('./basic/03_fileIO/data.json','wt') as f:
    json.dump(customer,f,indent=4)

with open('./basic/03_fileIO/data.json','rt') as f:
    data = json.load(f)

print(data)
