import dill as pickle
import json
import base64

z = lambda x : x + x

print(z(2))

z = pickle.dumps(z)

print(zs)

z64b = base64.b64encode(zs)

print(z64b)


z64s = str(z64b,'utf-8')

print(z64s)

# json goes here

z64b2 = bytes(z64s,'utf-8')

print(z64b2)

zs2 = base64.b64decode(z64b2)

print(zs2)

#print(z64s)

#data = {"z64s" : str.decode(z64s)}

#j = json.dumps(data)

#print(j)

#data2 = json.loads(j)

#print(data2)

#z64s2 = data2['z64s']

#zs2 = base64.b64decode(z64s2)

#print(zs2)

zz = pickle.loads(zs2)

print(zz(2))