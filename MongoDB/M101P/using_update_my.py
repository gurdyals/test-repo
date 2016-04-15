import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
        
# add a review date to a single record using update_one
def add_review_date_using_update_one(student_id):

    print "updating record using update_one and $set"
    # get a handle to the school database
    db=connection.school
    scores = db.scores

    try:
        # get the doc
        score = scores.find_one({'student_id':student_id, 'type':'homework'})
        print "before: ", score

        # update using set
        record_id = score['_id']
        result = scores.update_one({'_id':record_id},
                          {'$set':{'review_date':datetime.datetime.utcnow()}})
        print "num matched: ", result.matched_count

        score = scores.find_one({'_id':record_id})
        print "after: ", score

    except Exception as e:
        raise


# add a review date to all records
def add_review_dates_for_all():

    print "updating record using update_one and $set"
    # get a handle to the school database
    db=connection.school
    scores = db.scores

    try:
        # update all the docs
        result = score = scores.update_many({},{'$set':{'review_date':datetime.datetime.utcnow()}})
        print "num matched: ", result.matched_count

    except Exception as e:
        raise



########################################################################
##### def using_set():
#####  Quiz: PyMongo: Updating
##### In the following code fragment, what is the python expression in place of xxxx to set a new key "examiner" to be "Jones"
##### Please use the $set operator.
def using_set():

    print "updating record using set"
    # get a handle to the school database
    db=connection.school
    scores = db.scores


    try:
        # get the doc
        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "before: ", score

        # update using set
        scores.update_one({'student_id':1, 'type':'homework'}, { '$set' : { 'examiner' : 'Jones' } } )

        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise



#add_review_date_using_update_one(1)
##### add_review_dates_for_all()

using_set()

