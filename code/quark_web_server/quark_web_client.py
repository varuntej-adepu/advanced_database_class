#quark_client

import os.path
import dill as pickle
import quark_server
import json
import base64
import requests

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
	def __init__(self, host, path):
		self.host = host
		self.path = path

	def create(self, record):
		web_request = {
			"path" : self.path,
			"record" : json.dumps(record)
		}
		print(web_request)
		print("Client creating")
		result = requests.post(self.host + "/create", data=web_request)

	def read(self, select=everything, where=always):
		select_pkl = lambda_to_string(select)
		where_pkl = lambda_to_string(where)
		app_request = {
			'select_pkl' : select_pkl,
			'where_pkl': where_pkl
		}
		web_request = {
			"path" : self.path,
			"app_request" : json.dumps(app_request)
		}
		print(web_request)
		print("Client read")
		result = requests.post(self.host + "/read", data=web_request)
		if result.status_code != 200:
			return None
		print(result.text)
		result = json.loads(result.text)
		return result

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