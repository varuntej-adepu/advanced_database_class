import sqlite3
from bottle import route, run, get, post, template, request, default_app

db_file = "/home/drdelozier/mysite/todo.db"

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/hello/<name>')
def hello(name):
    return 'Hello ' + name + ' from Bottle!'

@route('/goodbye/<name>')
def goodbye(name):
    return template("goodbye.tpl", name=name)

@route('/todo')
def todo_list():
	conn = sqlite3.connect(db_file)
	c = conn.cursor()
	c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
	result = c.fetchall()
	# return str(result)
	output = template('make_table', rows=result)
	return output

@route('/new', method='POST')
def post_new_item():
    task = request.POST.task.strip()
    if not (type(task) is str):
        return '<p>Todo must be a string.</p>'
    if len(task) == 0:
        return '<p>Todo must not be empty.</p>'

    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (task,1))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

@route('/new', method='GET')
def new_item():
	return template('new_task.tpl')

application = default_app()
