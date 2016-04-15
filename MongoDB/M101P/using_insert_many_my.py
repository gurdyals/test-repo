#####  Quiz: PyMongo: Insert_many
##### Suppose you ran the following python program. How many documents would you expect to find in the things collection at the completion of the program, and why?


import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


def insert_many():

    # get a handle to the school database
    db=connection.test
    things = db.things

    # empty the collection
    things.drop()
    print "things.drop() :"
    print_things()
    cur = things.find()
    for doc in cur:
        print doc

    print "things.drop() : After"

    # insert some docs

    docs = [{'_id':1,'a':1}, 
            {'_id':2,'b':2},            
            {'_id':3,'b':3},            
            {'_id':3,'b':4},            
            {'_id':4,'b':5}]


    try:
        ##### things.insert_many(docs)
        things.insert_many( docs, ordered = False )

    except Exception as e:
        print "Unexpected error:", type(e), e


def print_things():
    # get a handle to the school database
    db=connection.test
    things = db.things

    cur = things.find()
    for doc in cur:
        print doc

print "Before the insert_many, here are the things"
print_things()
insert_many()
print "\n\nAfter the insert_many, here are the things"
print_things()


##### insert_many()


quit()

########################################################################
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


def insert_many():

    # get a handle to the school database
    db=connection.school
    people = db.people

    print "insert_many, reporting for duty"

    andrew = {"_id":"erlichson", "name":"Andrew Erlichson", "company":"MongoDB",
              "interests":['running', 'cycling', 'photography']}

    richard ={"name":"Richard Kreuter", "company":"MongoDB",
              "interests":['horses', 'skydiving', 'fencing']}    

    ##### people_to_insert = [andrew,richard]
    people_to_insert = [richard, andrew]


    try:
        ##### people.insert_many(people_to_insert,ordered=False)
        people.insert_many( people_to_insert, ordered = True )

    except Exception as e:
        print "\nUnexpected error:", type(e), e

def print_people():
    # get a handle to the school database
    db=connection.school
    people = db.people

    cur = people.find({},{'name':1})
    for doc in cur:
        print doc

print "Before the insert_many, here are the people"
print_people()
insert_many()
print "\n\nAfter the insert_many, here are the people"
print_people()

