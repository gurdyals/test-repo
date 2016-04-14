import re
import sys
import datetime




def writeList(list, filename, sep):
#     # with open(filename, "a") as f:
    with open(filename, "w") as f:
        for i in list:            
            f.write(i + sep + "\n")

def writeDict(dict, filename, sep):
#     # with open(filename, "a") as f:
    with open(filename, "w") as f:
#         # for i in dict.keys():            
        for i in sorted(dict, key=dict.get, reverse=True):
#             # f.write(i + " " + sep.join( [ str(x) for x in str( dict[i] ) ]) + "\n")
            f.write(i + "           " + sep + str ( dict[i] ) + "\n")

##### File "INBOX" contains one of my personal email folders
##### I am using this to create data visualisation of the emails
##### and some other stuff just for fun

fh = open ( 'INBOX' )

print "fh :", fh, ":"

d_word = dict()
l_word = list()

print "d_word :", d_word, ":"
print "l_word :", l_word, ":"


##################################
## 1)

i = fh.read()
# print i

# if re.findall ( '\S+@\S+', i )
##### l_word = re.findall ( '\S+@\S+\.\S+', i.lower() )

l_word = re.findall ( "from: .*?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9]{2,})", i.lower() )

# Regular expression  for an email is 
#  WebSite is    "http://www.regular-expressions.info/email.html"
#  \b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b
# This is email regexp for python
# from the WebSite "http://emailregex.com/"
#   r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# MODIFIED BETTER ONE IS BELOW
#   r"From.*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9]{2,})"



print "Len(l_word) :", len(l_word), ":"

l1 = list()
for i in l_word:
  print i
  i = re.split( '<|>|;', i )
  print "After re.split ( multi delimiters ) i iiiiii :", i, i[0]

  i = ''.join(i)

  print "Now sdskj  append i iiiiii :", i
  l1.append(i)

print "len(l_word) :", len(l_word)
print "len(l1) :", len(l1)



for email in l_word :
  d_word[ email ] = d_word.get( email, 0 ) + 1
  # d_word[ email.lower() ] = d_word.get( email.lower(), 0 ) + 1

print "len(d_word) :", len(d_word), ":"

d1 = dict()
d0 = dict()
for email in l1 :
  em = email.split('@')
  print "email :", email, email[0], email[1]
  print "em :", em, em[0], em[1]

  d1[ em[1] ] = d1.get( em[1], 0 ) + 1
  d0[ em[0] ] = d0.get( em[0], 0 ) + 1
  # d1[ email.lower() ] = d1.get( email.lower(), 0 ) + 1

print "len(d1) :", len(d1), ":"

# d1 = sorted(d_word, key=d_word.get, reverse=True)
# print type(d1)

q = 0
for k, v in d_word.items():
  if q < 11 :
    print k, v
  q = q + 1


l_word.sort(reverse=True)
writeList(l_word, 'l_word.txt', "  :")

l1.sort(reverse=True)
writeList(l1, 'l1_word.txt', "  :")

# fhand = open ( 'l_word.txt', 'wb' )
# fhand.write ( str(l_word) )
# fhand.close()

writeDict(d_word, 'd_word.txt', " ,")

writeDict(d1, 'd1_word.txt', " ,")



i = 1
f1 = open('d1word.js', 'w')

with open('dword.js', "w") as f:
  for key in sorted(d_word, key=d_word.get, reverse=True):
    key1 = key.split('@')
    print "Key1 : ", key1, key1[0], key1[1]

    if i < 1:
      # f.write( ",\n{text: '" + key[:10] + "', size: " + str( ( d_word[key] / 2 ) + 1 ) + "}")
      f.write( ",\n{text: '" + key1[0][:10] + "', size: " + str( d_word[key] ) + "}")

      f1.write( ",\n{text: '" + key1[1] + "', size: " + str( d_word[key] ) + "}")
    else:
      # f.write(  "dword = [{text: '" + key[:10] + "', size: " + str( ( d_word[key] / 2 ) + 1 ) + "}")
      f.write(  "dword = [{text: '" + key1[0][:10] + "', size: " + str( d_word[key] ) + "}")

      f1.write(  "dword = [{text: '" + key1[1] + "', size: " + str( d_word[key] ) + "}")
      i = 0
  f.write( "\n];" )

  f1.write( "\n];" )

  f.close()
  f1.close()

# {text: 'sakai', size: 100},



i = 1
with open('dword.js', "w") as f:
  for key in sorted(d0, key=d0.get, reverse=True):
    if i < 1:
      # f.write( ",\n{text: '" + key[:21] + "', size: " + str( d0[key] ) + "}")
      f.write( ",\n{text: '" + key[:21] + "', size: " + str( ( d0[key] / 3 ) + 1 ) + "}")
    else:
      # f.write(  "dword = [{text: '" + key[:21] + "', size: " + str( d0[key] ) + "}")
      f.write(  "dword = [{text: '" + key[:21] + "', size: " + str( ( d0[key] / 3 ) + 1 ) + "}")
      i = 0
  f.write( "\n];" )



i = 1
with open('d1word.js', "w") as f:
  for key in sorted(d1, key=d1.get, reverse=True):
    if i < 1:
      # f.write( ",\n{text: '" + key + "', size: " + str( d1[key] ) + "}")
      f.write( ",\n{text: '" + key + "', size: " + str( ( d1[key] / 4 ) + 1 ) + "}")
    else:
      # f.write(  "d1word = [{text: '" + key + "', size: " + str( d1[key] ) + "}")
      f.write(  "d1word = [{text: '" + key + "', size: " + str( ( d1[key] / 4 ) + 1 ) + "}")
      i = 0
  f.write( "\n];" )




quit()

## 1)
##################################

q = 0

for line in fh :
  line = line.strip()
#  for i in line :
#    print i
  print line

  q = q + 1
  print q
  if q > 10 : quit()
  


d_word[ EMAIL ] = d_word.get( EMAIL, 0 ) + 1





##################################
## 2)
##### d1_word = { 'a' : 1, 'b' : 2, 'c' : 3 }
##### 
##### print d1_word.keys(), d1_word.values()
##### 
##### for i in d1_word.keys() :
#####   print i, d1_word[i]
#####   print [ str(x) for x in str(d1_word[i]) ]
##### #  print [ str(x) for x in d1_word[i] ]
##### 
##### 
##### writeDict(d1_word, 'd1_word.txt', " = ")
##### 
##### quit()
##### 
## 2)
##################################


##################################
## 3)


##### dt_time = datetime.datetime.now().isoformat()
##### 
##### print "dt_time :", dt_time

##### 
##### quit()
##### 
## 3)
##################################

