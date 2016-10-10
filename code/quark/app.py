from bottle import route, template, request, static_file

from quark import Database

host = "pythonanywhere"

if host == "pythonanywhere":
    from bottle import default_app
    site_path = "/home/drdelozier/mysite/"
else:
    from bottle import run
    site_path = "/home/greg/mysite/"

database_file = site_path + "todo3.pkl"
static_folder = site_path + "static"

db = Database(database_file)

@route('/')
@route('/todo')
def todo_list():
    items = db.read(where=lambda v: v['status'] == 1)
    result = []
    for todo in items:
        result.append((todo['id'],todo['task']))
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

    items = db.read()
    max_id = 0
    for item in items:
        if item['id'] > max_id:
            max_id = item['id']
    db.create({"id":max_id + 1, "task":task, "status":1})

    return template("confirmation.tpl", message='The new task was inserted into the database')

@route('/edit/<id>', method='GET')
def edit_task(id):
    items = db.read(where=lambda v: v['id'] == int(id))
    item = items[0]
    task = item['task']
    return template('edit_task.tpl', id=id, task=task)

@route('/edit', method='POST')
def post_edit_task():
    if request.POST.No == "No":
        return "<p>Edit request was cancelled.</p>"
    if request.POST.Yes != "Yes":
        return "<p>Edit request was not clear.</p>"
    id =  int(request.POST.id)
    task =  request.POST.task
    db.update({'task':task}, where=lambda v: v['id'] == int(id))
    return template("confirmation.tpl", message='Edit request was completed.')


"""

@route('/delete/<id>', method='GET')
def delete_task(id):
    query = Todo.select().where(Todo.id == id)
    result = []
    for todo in query:
        result.append((todo.id,todo.task))
    if len(result) != 1:
        return '<p>Expected one thing to delete.</p>'
    (id, task) = result[0]
    return template('delete_task.tpl', id=id, task=task)

@route('/delete', method='POST')
def post_delete_task():
    if request.POST.No == "No":
        return "<p>Delete request was cancelled.</p>"
    if request.POST.Yes != "Yes":
        return "<p>Delete request was not clear.</p>"
    id =  int(request.POST.id)
    db.delete({'task':task}, where=lambda v: v['id'] == int(id))
    #if i != 1:
    #    return "<p>Delete request was not completed, expected 1 record modified.</p>"
    return template("confirmation.tpl", message='Delete request was completed.')

@route('/static/<filename>')
def server_static(filename):
        return static_file(filename, root=static_folder)

#run()... #if localhost
"""
application = default_app() #if pythonanywhere
