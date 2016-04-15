
import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# removes all review dates
def remove_all_review_dates():
    print "\n\nremoving all review dates"

    # get a handle to the school database
    db=connection.school
    scores = db.scores
    try:
        result = scores.update_many({'review_date':{'$exists':True}},
                                    {'$unset':{'review_date':1}})
        print "Matched this number of docs: ", result.matched_count

    except Exception as e:
        print "Unexpected error:", type(e), e
        raise


        

# add a review date to single record using replace_one
def add_review_date_using_replace_one(student_id):

    # get a handle to the school database
    db=connection.school
    scores = db.scores

    print "updating record using replace_one"

    try:
        # get the doc
        score = scores.find_one({'student_id':student_id, 'type':'homework'})
        print "before: ", score

        print_dict(score)

        # add a review_date
        score['review_date'] = datetime.datetime.utcnow()

        # update the record with replace_one
        record_id = score['_id']
        scores.replace_one({'_id': record_id}, score)
        score = scores.find_one({'_id': record_id})
        print "after: ", score

        print_dict(score)

    except Exception as e:
        print "Unexpected error:", type(e), e
        raise



def print_dict(test_dict):
    if test_dict is not None:
        for key, val in test_dict.items(): print key, " : ", val
    else:
        print "Input  test_dict() :", test_dict




##### This function added for testing the dict {del and add methods}
def testing():
    test_d = { "_id" : "569a4d3ddbc1f33317e4c54c", "review_date" : "2016-01-17T05:07:50.823Z", "examiner" : "Jones", "student_id" : 1, "score" : 63.57353967304567, "type" : "homework" }

    print "\n1. Print test_d dict :"
    ##### for key, val in test_d.items(): print key, " : ", val
    print_dict(test_d)

    del(test_d['_id'])
    print "\n2. Print test_d [minus '_id'] dict :"
    ##### for key, val in test_d.items(): print key, " : ", val
    print_dict(test_d)

    del(test_d['review_date'])
    print "\n3. Print test_d [minus 'review_date'] dict :"
    ##### for key, val in test_d.items(): print key, " : ", val
    print_dict(test_d)

    del(test_d['type'])
    print "\n4. Print test_d [minus 'type'] dict :"
    ##### for key, val in test_d.items(): print key, " : ", val
    print_dict(test_d)

    test_d['_id'] = 'this is test id'
    print "\n5. Print test_d [Add '_id'] dict :"
    ##### for key, val in test_d.items(): print key, " : ", val
    print_dict(test_d)


remove_all_review_dates()
add_review_date_using_replace_one(1)

testing()
