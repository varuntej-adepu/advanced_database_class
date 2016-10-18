from bottle import route, request, run

import quark
import json
import dill as pickle
import base64

def string_to_lambda(z):
	z = bytes(z,'utf-8')
	z = base64.b64decode(z)
	x = pickle.loads(z)
	return x


@route('/create', method='POST')
def post_new_item():
    path = request.forms.get("path")
    record = request.forms.get("record")
    record = json.loads(record)
    print("create json = ",record)
    db = quark.Database(path)
    db.create(record)
    print("creating " + str(record) + " in " + path)

@route('/read', method='POST')
def post_new_item():
    path = request.forms.get("path")
    app_request = request.forms.get("app_request")
    app_request = json.loads(app_request)
    assert type(app_request) is dict
    select = string_to_lambda(app_request['select_pkl'])
    where = string_to_lambda(app_request['where_pkl'])
    db = quark.Database(path)
    results = db.read(select, where)
    results = json.dumps(results)
    return results

run(host='localhost', port=8080)
