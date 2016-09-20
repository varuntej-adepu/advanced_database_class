
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/hello/<name>')
def hello(name):
    return 'Hello ' + name + ' from Bottle!'

@route('/goodbye/<name>')
def goodbye(name):
    return template("goodbye.tpl", name=name)

application = default_app()

