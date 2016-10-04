import sqlite3
from bottle import route, template, request, static_file

host = "pythonanywhere"

if host == "pythonanywhere":
    from bottle import default_app
    site_path = "/home/drdelozier/mysite/"
else:
    from bottle import run
    site_path = "/home/greg/mysite/"

database_file = site_path + "todo.db"
static_folder = site_path + "static"

@route('/')
@route('/todo')
def todo_list():
	conn = sqlite3.connect(database_file)
	c = conn.cursor()
	c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
	result = c.fetchall()
	# return str(result)
	output = template('view_todos', rows=result)
	return output

@route('/new', method='GET')
def new_item():
	return template('new_task.tpl')

@route('/new', method='POST')
def post_new_item():
    task = request.POST.task.strip()
    if not (type(task) is str):
        return '<p>Todo must be a string.</p>'
    if len(task) == 0:
        return '<p>Todo must not be empty.</p>'

    conn = sqlite3.connect(database_file)
    c = conn.cursor()

    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (task,1))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

@route('/edit/<id>', method='GET')
def edit_task(id):
	conn = sqlite3.connect(database_file)
	c = conn.cursor()
	c.execute("SELECT task FROM todo WHERE id = ?",(id,))
	result = c.fetchall()
	if len(result) != 1:
	    return '<p>We expected to find one task where ID is %s</p>' % id
	task = str(result[0][0])
	return template('edit_task.tpl', id=id, task=task)

@route('/edit', method='POST')
def post_edit_task():
    if request.POST.No == "No":
        return "<p>Edit request was cancelled.</p>"
    if request.POST.Yes != "Yes":
        return "<p>Edit request was not clear.</p>"
    id =  int(request.POST.id)
    task =  request.POST.task
    #return str(id) + ":" + task
    conn = sqlite3.connect(database_file)
    c = conn.cursor()
    c.execute("UPDATE todo SET task = ? WHERE id = ?", (task, id))
    conn.commit()
    c.close()
    return "<p>Edit request was completed.</p>"

@route('/delete/<id>', method='GET')
def delete_task(id):
	conn = sqlite3.connect(database_file)
	c = conn.cursor()
	c.execute("SELECT task FROM todo WHERE id = ?",(id,))
	result = c.fetchall()
	if len(result) != 1:
	    return '<p>We expected to find one task where ID is %s</p>' % id
	task = str(result[0][0])
	return template('delete_task.tpl', id=id, task=task)

@route('/delete', method='POST')
def post_delete_task():
    if request.POST.No == "No":
        return "<p>Delete request was cancelled.</p>"
    if request.POST.Yes != "Yes":
        return "<p>Delete request was not clear.</p>"
    id =  int(request.POST.id)
    conn = sqlite3.connect(database_file)
    c = conn.cursor()
    c.execute("DELETE FROM todo WHERE id = ?",(id,))
    conn.commit()
    c.close()
    return "<p>Delete request was completed.</p>"

@route('/static/<filename>')
def server_static(filename):
        return static_file(filename, root=static_folder)

#run()... #if localhost
application = default_app() #if pythonanywhere
