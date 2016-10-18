from squeaker import Database

db = Database("/home/drdelozier/mysite/todo3.pkl")
db.create({"id":1,"task":"Check out this database.","status":0})
db.create({"id":2,"task":"Do something interesting.","status":1})
db.create({"id":3,"task":"Grade homework.","status":0})
db.create({"id":4,"task":"Buy groceries.","status":1})
db.create({"id":5,"task":"Commit this code.","status":1})
items = db.read()
print(items)
