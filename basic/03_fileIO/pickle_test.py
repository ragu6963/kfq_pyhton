import pickle
data = {1: "python", 2: "love"}

print(type(data))

with open("test.pickle", 'wb') as f:
    pickle.dump(data, f)

datab = pickle.dumps(data)
print(type(datab))

with open("test.pickle", "rb") as f:
    data = pickle.load(f)
    print(data)