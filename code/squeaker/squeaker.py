import os.path
import pickle

def always(v):
    return True

def everything(v):
    return v

class Database:
    def __init__(self, path):
        self._path_ = path
        if os.path.isfile(self._path_):
            with open(self._path_,"rb") as f:
                self._data_ = pickle.load(f)
        else:
            self._data_ = []

    def commit(self):
        with open(self._path_,"wb") as f:
            pickle.dump(self._data_,f)

    def create(self, record):
        self._data_.append(record)
        self.commit()

    def read(self, select=everything, where=always):
        results = []
        for item in self._data_:
            if where(item):
                results.append(select(item))
        return results

    def update(self, values={}, where=always):
        for item in self._data_:
            if where(item):
                for key in values:
                    item[key] = values[key]
        self.commit()

    def delete(self, where=always):
        copy = []
        for item in self._data_:
            if not where(item):
                copy.append(item)
        self._data_ = copy
        self.commit()

if __name__ == "__main__":
    db = Database("/home/drdelozier/kent/advanced_database_class/code/squeaker/pets.pkl")
    db.create({"name":"Squeakers","type":"guinea pig"})
    db.create({"name":"Clarabelle","type":"cow"})
    db.create({"name":"Dorothy","type":"dog"})
    db.create({"name":"Hopper","type":"rabbit"})
    items = db.read(where=lambda v: "a" in v["name"])
    print(items)

    items = db.read()
    print(items)

    items = db.read(select=lambda v: {"name":v['name'].lower()} ,where=lambda v: "a" in v["name"])
    print(items)

    db.delete(where=lambda v:v["name"] == "Hopper")
    print(db.read())

    db.update(values = {"name":"Suzy"}, where=lambda v: v["name"] == "Dorothy")
    print(db.read())

    print("done")
