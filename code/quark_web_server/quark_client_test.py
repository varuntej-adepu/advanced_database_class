import unittest
import quark_web_client
import os

class TestQuarkDatabaseClient(unittest.TestCase):
    
    def setUp(self):
        # we know that this is the localhost file
        if os.path.isfile("pets.pkl"):
            os.remove("pets.pkl")
        self.db = quark_web_client.Database("http://localhost:8080", "pets.pkl")
        self.db.create({"name":"Squeakers","type":"guinea pig"})
        self.db.create({"name":"Clarabelle","type":"cow"})
        self.db.create({"name":"Dorothy","type":"dog"})
        self.db.create({"name":"Hopper","type":"rabbit"})

    def xtest_00_do_nothing(self):
        xpass
        
    def test_00_create(self):
        #items = self.db.read(select = lambda v:v, where=lambda v:True)
        items = self.db.read()
        print(items)
        self.assertTrue(len(items) == 4)
        for item in items:
            self.assertTrue("name" in item)
            self.assertTrue("type" in item)
            self.assertTrue(type(item['name']) is str)
            self.assertTrue(type(item['type']) is str)
        found = False
        for item in items:
            if item["name"] == "Clarabelle":
                self.assertTrue(item["type"] == "cow")
                found = True
        self.assertTrue(found == True)        

    def xtest_01_read(self):
        items = self.db.read(where=lambda v: "a" in v["name"])
        self.assertEqual(len(items),2)
        items = self.db.read(
                select = lambda v: {"name":v['name'].lower()},
                where  = lambda v: "a" in v["name"])
        self.assertEqual(len(items),2)
        found = False
        for item in items:
            self.assertTrue(len(item) == 1)
            self.assertTrue("name" in item)
            if item["name"] == "clarabelle":
                found = True
        self.assertTrue(found == True)        

    def xtest_02_delete(self):
        self.db.delete(where=lambda v:v["name"] == "Hopper")
        items = self.db.read()
        self.assertTrue(len(items) == 3)

    def xtest_03_update(self):        
        items = self.db.read()
        self.assertTrue(len(items) == 4)
        found_dorothy = False
        found_suzy = False
        for item in items:
            if item["name"] == "Dorothy":
                found_dorothy = True
            if item["name"] == "Suzy":
                found_suzy = True
        self.assertTrue(found_dorothy == True)        
        self.assertTrue(found_suzy == False)        
        self.db.update(
            values = {"name":"Suzy"}, 
            where=lambda v: v["name"] == "Dorothy")
        items = self.db.read()
        self.assertTrue(len(items) == 4)
        found_dorothy = False
        found_suzy = False
        for item in items:
            if item["name"] == "Dorothy":
                found_dorothy = True
            if item["name"] == "Suzy":
                found_suzy = True
        self.assertTrue(found_dorothy == False)        
        self.assertTrue(found_suzy == True)        

        
if __name__ == "__main__":
    unittest.main(verbosity=2)