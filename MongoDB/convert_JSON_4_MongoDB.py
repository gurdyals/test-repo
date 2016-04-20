# Written by :     Gurdyal Singh
# Written on :     April 16, '2016
# Description :    Pretty Print a JSON file into another FILE or STRING
#                  Input DATA File is though JSON format
#                  but its a list of TWO DICTIONARIES
#                  with KEYS = ( 1.FIELDS, 2.DATA )
#                  DATA is a LIST of DICTIONARY'ies
#                  MongoDB expects each RECORD as a DICTIONARY on each
#                  SINGLE LINE.
#                  This PYTHON program tries to convert this INPUT JSON
#                  file in a JSON format acceptable for use with MongoDB
#                  tool mongoimport
#                  Convert a list of Values into MongoDB JSON format
# Completed on :   April 17, 2016
# Total Days  :    Approximately 20 Hours




# https://docs.python.org/2/library/pprint.html
# On Command Line use "cat some.json | python -m json.tool"

import pprint
import json





fh = open ( 'Blood_bank_updated-sep_2015.json', 'r' )

########################################################################
# use "json" module
# 4)

#  To parse a STRING use "json.loads"
#  To parse a FILE   use "json.load"
#     Please note the difference is load[s] - s for string

json_bb = json.load( fh )

print 'json_bb :', type(json_bb)
print "\n\n"

##### var_i = 0
##### for key in json_bb.keys():
#####   var_i = var_i + 1
#####   print var_i, key

fields = range ( len( json_bb['fields'] ) )
var_i = 0
for label in json_bb['fields']:
  fields[var_i] = label['label']
  var_i = var_i + 1
  # print var_i, label['label'], label

# Change "id" to "_id" for use as MongoDB "_id"
if fields[0] == "id":
  fields[0] = "_id"

##### print "\n\n\n"
# print "Data : ", json_bb['data']

##### print "fields :", fields
##### print "\n\n  len( fields )   :", len(fields)


fhand = open("BB_MongoDB.json", 'wb')
##### fh1 = open("BB_MongoDB_test.json", 'wb')

#####  Comment Next line as it is not required currently
##### bb_mongo = list()

var_i = 0
for values in json_bb['data']:
  rec = list()
  values[0] = int( values[0] )
  for index in range( len( fields ) ):
    ##### print "Index :", index, "fields :", fields[index], "values :", values[index], type( values[index] )
    rec.append( ( fields[index], values[index] ) )

  temp_data = dict( rec )
  print "\n\ntype(temp_data) :", type(temp_data), temp_data

#####  Comment Next line as it is not required currently
#####  bb_mongo.append( temp_data )

  ##### json.dump ( use "indent = 0" to print records in different lines )
  ##### json.dump( temp_data, fh1, sort_keys = True, indent = 0 )

  fhand.write( json.dumps( temp_data ) + u"\n" )
  ##### fhand.write( json.dumps( temp_data, sort_keys = True, ensure_ascii = False ) + u"\n" )

  if var_i < 22:
      print var_i, "Values :", values, "\n\n"
      print "\n\nRecord :" , rec
#####  Comment Next line as it is not required currently
      ##### print "\n\n\nIndex :", var_i, "Mongo_BB :" , bb_mongo
  var_i += 1


# fhand = open("BB_MongoDB.json", 'w')
#   json.dump(bb_mongo, fhand, sort_keys = True)

# with open("BB_MongoDB.with_open", 'w') as outfile:
#   json.dump(bb_mongo, outfile)





quit()

# 4)
########################################################################



########################################################################
# use "pprint" module 
# 1)
##### Set  the variables for PrettyPrinter for pprint as per
##### class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None)
##### "stream" is the file handle to write the OutPut

pp = pprint.PrettyPrinter(indent = 4, width = 100, depth = 7)
##### Close the setup of PrettyPrinter from pprint
##### set "PrettyPrinter" method in "pprint" Module

str_bb = fh.read()



out_bb = pp.pprint ( str(str_bb) )

print str_bb, "\n\n\n\n\n ####################### \n\n\n\n\n\n", str ( str_bb )

print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", "\n\n\n\n\n"

print "out_bb : ", str ( out_bb )


quit()

# 1)
########################################################################




########################################################################
# 3)
# On Command Line use 
#       cat some.json | python -m json.tool

# 3)
########################################################################




########################################################################
# use "json" module
# 2)
# json_bb1 = json.dumps(json_bb, indent = 4, sort_keys = False/True)

#  To parse a STRING use "json.loads"
#  To parse a FILE   use "json.load"
#     Please note the difference is load[s] - s for string

json_bb = json.load( fh )

# print json.dumps(json_bb, indent = 4, sort_keys = False)

json_bb1 = json.dumps(json_bb, indent = 4, sort_keys = False)

# print "json_bb1 :", "\n\n\n\n\njson.dumps :", json_bb1
# print "\n\n\n\n\n", json_bb1


j = {}
i = json.loads(json_bb1)
# k = eval(json_bb1)

print 'json_bb :', type(json_bb), "type(json_bb1) :", type(json_bb1), "j :", type(j), "i :", type(i) #, "k :", type(k)

print "\n\n\n\n\n"


j = 0
for i in json_bb.keys():
  j = j + 1
  print j, i

# print "\n\n\n\n\n"


j = 0
for i in json_bb.values():
  j = j + 1
#   print j, i

# print "\n\n\n\n\n"

# print json_bb['fields'], len( json_bb['fields'] )

seq = range ( len( json_bb['fields'] ) )
# seq = range( 100 ) # This creates a list with 100 elements

j = 0
for i in json_bb['fields']:
  seq[j] = i['label']
  j = j + 1
  # print j, i
  # print i['label']


print "\n\n\n\n\n"

print "seq :", seq
print "\n\n                len( seq )   :", len(seq)



temp_d = dict.fromkeys(seq)

print "\n\n\n\n\n"
print "type temp_d :", type(temp_d), temp_d

temp_d1 = dict.fromkeys(seq, 100)

print "\n\n\n\n\n"
print "type temp_d1 :", type(temp_d1), temp_d1

values = range ( len ( seq ) )


temp_d2 = dict.fromkeys(seq, values)

print "\n\n\n\n\n"
print "type values :", type(values), values
print "type temp_d2 :", type(temp_d2), temp_d2


temp_d3 = dict.fromkeys(seq, values)

print "\n\n\n\n\n"
print "type values :", type(values), values
print "type temp_d3 :", type(temp_d3), temp_d3


seq1 = seq

for i in range( len(seq) ):
  seq1[i] = ( seq[i], values[i] )
  print i, seq[i], values[i]


print type(seq), type(seq1), "\n\n :", seq, "\n\n\n :", seq1

temp_d3 = dict(seq1)


print "\n\n\n\n\n"
print "type values :", type(values), values
print "type temp_d3 :", type(temp_d3), temp_d3





quit()

# 2)
########################################################################

