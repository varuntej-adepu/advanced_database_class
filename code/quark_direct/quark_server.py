import os.path
import dill as pickle
import quark
import json
import base64

def string_to_lambda(z):
	z = bytes(z,'utf-8')
	z = base64.b64decode(z)
	x = pickle.loads(z)
	return x

def always(v):
	return True

def everything(v):
	return v

class Database:
	def __init__(self, request):
		data = json.loads(request)
		print("Server request = ", data)
		self.db = quark.Database(data['path'])

	def create(self, request):
		data = json.loads(request)
		record = data['record']
		print("Server creating...")
		self.db.create(record)

	def read(self, request):
		print("Server reading...")
		data = json.loads(request)
		select = string_to_lambda(data['select_pkl'])
		where  = string_to_lambda(data['where_pkl'])
		result = self.db.read(select, where)
		return(json.dumps(result))

	def update(self, request):
		print("Server deleting...")
		data = json.loads(request)
		values = data['values']
		where  = string_to_lambda(data['where_pkl'])
		result = self.db.update(values, where)
		return(json.dumps(result))

	def delete(self, request):
		print("Server deleting...")
		data = json.loads(request)
		where  = string_to_lambda(data['where_pkl'])
		result = self.db.delete(where)
		return(json.dumps(result))
		
if __name__ == "__main__":
	pass