#quark_client

import os.path
import dill as pickle
import quark_server
import json
import base64

def always(v):
	return True

def everything(v):
	return v

def lambda_to_string(x):
	z = pickle.dumps(x)
	z = base64.b64encode(z)
	z = str(z,'utf-8')
	return z

class Database:
	def __init__(self, path):
		request = {'path':path}
		request = json.dumps(request)
		print("Client request = ",request)
		self.db = quark_server.Database(request)

	def create(self, record):
		request = json.dumps({'record':record})
		print("Client creating")
		self.db.create(request)

	def read(self, select=everything, where=always):
		select_pkl = lambda_to_string(select)
		where_pkl = lambda_to_string(where)
		request = json.dumps({
			'select_pkl' : select_pkl,
			'where_pkl': where_pkl
		})
		print("Sending read request ", request)
		result = self.db.read(request)
		return json.loads(result)

	def update(self, values={}, where=always):
		where_pkl = lambda_to_string(where)
		request = json.dumps({
			'values': values,
			'where_pkl': where_pkl
		})
		print("Sending update request ", request)
		result = self.db.update(request)
		return json.loads(result)

	def delete(self, where=always):
		where_pkl = lambda_to_string(where)
		request = json.dumps({
			'where_pkl': where_pkl
		})
		print("Sending delete request ", request)
		result = self.db.delete(request)
		return json.loads(result)

if __name__ == "__main__":
	pass