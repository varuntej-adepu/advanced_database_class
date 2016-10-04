import sqlite3
from bottle import route, template, request, static_file

from peewee import *

host = "pythonanywhere"

if host == "pythonanywhere":
    from bottle import default_app
    site_path = "/home/drdelozier/mysite/"
else:
    from bottle import run
    site_path = "/home/greg/mysite/"

database_file = site_path + "todo2.db"
static_folder = site_path + "static"

db = SqliteDatabase(database_file)

class Todo(Model):
    id = PrimaryKeyField()
    task = TextField()
    status = IntegerField()

    class Meta:
        database = db # This model uses the "todo2.db" database.

db.connect()

@route('/')
@route('/todo')
def todo_list():
    query = Todo.select().where(Todo.status == 1)
    result = []
    for todo in query:
        result.append((todo.id,todo.task))
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
    todo = Todo(task=task, status=1)
    todo.save()
    return template("confirmation.tpl", message='The new task was inserted into the database')

@route('/edit/<id>', method='GET')
def edit_task(id):
    todo = Todo.select().where(Todo.id == id).get()
    task = todo.task
    return template('edit_task.tpl', id=id, task=task)

@route('/edit', method='POST')
def post_edit_task():
    if request.POST.No == "No":
        return "<p>Edit request was cancelled.</p>"
    if request.POST.Yes != "Yes":
        return "<p>Edit request was not clear.</p>"
    id =  int(request.POST.id)
    task =  request.POST.task
    todo = Todo.select().where(Todo.id == id).get()
    todo.task = task
    todo.save()
    return template("confirmation.tpl", message='Edit request was completed.')

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
    todo = Todo.select().where(Todo.id == id).get()
    i = todo.delete_instance()
    if i != 1:
        return "<p>Delete request was not completed, expected 1 record modified.</p>"
    return template("confirmation.tpl", message='Delete request was completed.')

@route('/static/<filename>')
def server_static(filename):
        return static_file(filename, root=static_folder)

#run()... #if localhost
application = default_app() #if pythonanywhere
