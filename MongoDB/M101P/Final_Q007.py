import pymongo


connection = pymongo.MongoClient ( "mongodb://localhost" )


db = connection.test 
album = db.albums 
image = db.images



icur = image.find ( { } )
icur.sort ( '_id', pymongo.ASCENDING )


count = 0
for i in icur :
    count += 1
    print "\n", count, ":) ", i, " : _id : ", i['_id'], " :"

    id = i['_id']
    ##### id = 555511

    result = album.find_one ( { 'images' : id } )
    print "result Attr : ", result, " :"

#####    print "\n\nacknowledged : ", result.acknowledged, " : "
#####    print "matched_count : ", result.matched_count, " : "
#####    print "modified_count : ", result.modified_count, " : " 
#####    print "raw_result : ", result.raw_result, " : " 
#####    print "upserted_id : ", result.upserted_id, " : \n\n\n"
#####    print "result['n'] : ", result['n'], " : \n\n\n"

    atr1 = 0
    if result is not None :
        ##### for atr in result :
            atr1 += 1
            print "\nATTR :", atr1, " : ", count, ":) " ##### , atr, " :"
    else :
        res1 = db.res1.update_one ( { '_id' : 'Delete' }, { '$addToSet' : { 'image_id' : id } }, upsert = True )
        print "addToSet result.update_one : ", id, " :"
        print "res1 : ", res1, " :"

        print "\n\nacknowledged : ", res1.acknowledged, " : "
        print "matched_count : ", res1.matched_count, " : "
        print "modified_count : ", res1.modified_count, " : " 
        print "raw_result : ", res1.raw_result, " : " 
        print "upserted_id : ", res1.upserted_id, " : \n\n\n"
        ##### print "result['n'] : ", res1['n'], " : \n\n\n"

        res2 = image.delete_one( { '_id' : id } )

        print "\n\nacknowledged : ", res2.acknowledged, " : "
        print "deleted_count : ", res2.deleted_count, " : " 
        print "raw_result : ", res2.raw_result, " : " 
        ##### print "result['n'] : ", res2['n'], " : \n\n\n"


res0 = db.res1.find_one( )

print "res0 : ", res0, " :\n\n\n\n\n"

##### for i in res0 :
#####     print "res0 : ", i, " :"
#####     image = i['image_id']
#####     print "Image : ", image, " :"
#####     print type(image)


print "res0 : ", res0, " :"
image = res0['image_id']
print "Image : ", image, " :"
print "\n\n\n\n\n\n\n\n : ", type(image), " : Length ( image ) : ", len(image), " : \n\n\n\n\n"

tot = 100000

print "Total : ", tot, " : minus : ", len(image), " : equal : ", tot - len(image), " :"


    ##### if count > 12 : break

quit()




> db.images.count()
89737
> db.images.find( { tags : 'kittens' } ).count()
44822
> 

