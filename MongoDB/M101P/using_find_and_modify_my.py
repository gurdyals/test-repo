# Andrew Erlichson
# MongoDB, Inc. Copyright 2015 - All Rights Reserved

import pymongo

# gets the next number in a sequence
def get_next_sequence_number(name):
    connection = pymongo.MongoClient("mongodb://localhost")

    db = connection.test
    counters = db.counters

    # let's get ourselves a sequence number
    # note there are two other varients of this call as well:
    # find_one_and_delete
    # find_one_and_replace
    # all these map to the the command find_and_modify

    
    try: 
        counter = counters.find_one_and_update(filter={'type':name}, 
                                               update={'$inc':{'value':11}}, 
                                               upsert=True,
                                               return_document=pymongo.ReturnDocument.AFTER)
        print_dict(counter)


    except Exception as e:
        print "Exception: ", type(e), e

    counter_value = counter['value']
    return counter_value


def print_dict(test_dict):
    if test_dict is not None:
        for key, val in test_dict.items(): print key, " : ", val
    else:
        print "Input  test_dict() :", test_dict



print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
