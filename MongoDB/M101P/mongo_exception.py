import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Andrew', 'lastname':'Erlichson'}
print doc
print "about to insert the document"

try:
    users.insert_one(doc)
except Exception as e:
    print "insert failed:", type(e), " : ", e, " :"

print doc
print "inserting again"
##### doc = {'firstname':'Andrew', 'lastname':'Erlichson'}

try:
    users.insert_one(doc)
except Exception as e:
    print "second insert failed:", type(e), " : ", e, " :"

print doc

try:
  ##### users.drop()
  print "Pretty Printing : "
  ##### users.find().pretty()
  ##### users.find().show()
  users.find()
except Exception as e:
  print "Dropping Failed : ", type(e), " : ", e, " :"


iter = users.find()

for item in iter:
  print item
  print item["_id"]
  print item['firstname']
  print item['lastname']
  ##### print item[value]
