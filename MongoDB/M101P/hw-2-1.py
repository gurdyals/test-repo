#####  Homework: Homework 2.1

##### In this problem, you will be using a collection of student scores that is similar to what we used in the lessons. Please download grades.json from the Download Handout link and import it into your local mongo database as follows:

#####     mongoimport -d students -c grades < grades.json

##### The dataset contains 4 scores for 200 students.

##### First, let's confirm your data is intact; the number of documents should be 800.

#####     use students
#####     db.grades.count()

##### You should get 800.

##### This next query, which uses the aggregation framework that we have not taught yet, will tell you the student_id with the highest average score:

#####     db.grades.aggregate({'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1})

##### The answer should be student_id 164 with an average of approximately 89.3.

##### Now it's your turn to analyze the data set. Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest.

##### What is the student_id of the lowest exam score above 65?






########################################################################
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades


def find():

    print "find, reporting for duty"

    query = { 'score' : { '$gt' : 65 }, 'type' : 'exam' }
    ##### query = { 'score' : { '$gt' : 65 } }

    try:

        cursor = grades.find(query)
        ##### cursor = grades.find(query) ##### .skip(4)
        cursor = cursor.limit(1)

        #cursor = cursor.sort('student_id', pymongo.ASCENDING).skip(4).limit(1)
        
        cursor = cursor.sort( 'score', pymongo.ASCENDING )



    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc
        print_dict(doc)



def find_one():

    print "find one, reporting for duty"
    query = {'score':10}
    
    try:
        doc = grades.find_one(query)
        
    except Exception as e:
        print "Unexpected error:", type(e), e

    
    print doc
    print_dict(doc)




def print_dict(test_dict):
    if test_dict is not None:
        for key, val in test_dict.items(): print key, " : ", val
    else:
        print "Input  test_dict() :", test_dict




find()
##### find_one()

