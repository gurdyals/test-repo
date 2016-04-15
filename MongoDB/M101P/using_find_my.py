#####  Quiz: PyMongo: find, find_one and Cursors
##### Consider the following code snippet:

import pymongo
import sys

# establish a connection to the server, and use it to get a handle on the scores collection.
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database and the scores collection.
db=connection.school
scores = db.scores
     
##### Please enter the one line of python code that would be needed in place of XXX to find one document in the collection and have it print out properly.
##### Constraints due to the limits of our parser: use scores (the Collection object), but not db or connection, in your answer. Do not include any arguments in your query.

try:
        ##### XXX
        doc = scores.find_one()
        
except Exception as e:
        print "Unexpected error:", type(e), e

print doc


quit()


########################################################################
########################################################################
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
scores = db.scores


def find():

    print "find, reporting for duty"

    query = {'type':'exam'}

    try:
        cursor = scores.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break
        


def find_one():

    print "find one, reporting for duty"
    query = {'student_id':10}
    
    try:
        doc = scores.find_one(query)
        
    except Exception as e:
        print "Unexpected error:", type(e), e

    
    print doc



while True:
  choice = int(raw_input("Print your choice : "))
  print "Choice : ", choice, type (choice)
  if choice == 1:
    print " find() "
    find()
  if choice == 2:
    print " find_one() "
    find_one()
  else:
    break
