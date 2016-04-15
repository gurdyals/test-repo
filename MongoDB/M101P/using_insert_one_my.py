import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

#####  Quiz: PyMongo: Insert_one
##### Do you expect the second insert below to succeed?

# get a handle to the school database
db=connection.school
people = db.people

doc = {"name":"Andrew Erlichson", "company":"MongoDB",
              #"interests":['running', 'cycling', 'photography']}
              "interests":['funning', 'fyling', 'forhorphy']}

try:
        print "1. doc :", doc, ":"

        people.insert_one(doc)   # first insert
        print "2. doc['_id'] :", doc['_id'], ":"

        del( doc['_id'] )
        print "3. doc :", doc, ":"

        people.insert_one(doc)   # second insert
        print "4. doc :", doc, ":"

except Exception as e:
        print "Unexpected error:", type(e), e



quit()


########################################################################
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


def insert():

    # get a handle to the school database
    db=connection.school
    people = db.people

    print "insert, reporting for duty"

    richard ={"name":"Richard Kreuter", "company":"MongoDB",
              "interests":['horses', 'skydiving', 'fencing']}    
    andrew = {"_id":"erlichson", "name":"Andrew Erlichson", "company":"MongoDB",
              "interests":['running', 'cycling', 'photography']}


    try:
        people.insert_one(richard)
        people.insert_one(andrew)

    except Exception as e:
        print "Unexpected error:", type(e), e

    print(richard)
    print(andrew)




insert()

