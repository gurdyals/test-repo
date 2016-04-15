#!/usr/bin/env python

import pymongo
import gridfs

# establish a connection to the database
connection = pymongo.MongoClient()

#get a handle to the test database
db = connection.test
file_meta = db.file_meta
file_used = "sample_128_mb.txt"
vmtext = "vmtext"

def main():

    grid = gridfs.GridFS(db, "text")
    fin = open(file_used, "r")
    vm = open(vmtext, "r")

    _id = grid.put(fin)
    _id1 = grid.put(vm)
    fin.close()
    vm.close()

    print "id of file is", _id
    print "id1 of file is", _id1

    file_meta.insert( { "grid_id": _id, "filename": file_used})
    file_meta.insert( { "grid_id": _id1, "filename": vmtext})

if __name__ == '__main__':
    main()
