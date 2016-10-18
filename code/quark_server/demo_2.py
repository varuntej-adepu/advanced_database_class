import dill as pickle
import json
import base64

def lambda_to_string(x):
	z = pickle.dumps(x)
	z = base64.b64encode(z)
	z = str(z,'utf-8')
	return z
	
def string_to_lambda(z):
	z = bytes(z,'utf-8')
	z = base64.b64decode(z)
	x = pickle.loads(z)
	return x

f = lambda x : x * x

s = lambda_to_string(f)

g = string_to_lambda(s)

print(g(3))
