import json
import urllib2
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db=connection.reddit
stories = db.stories

# drop existing collection
stories.drop()

# get the reddit home page
reddit_page = urllib2.urlopen("https://www.reddit.com/r/technology/.json")

print "reddit_page :", reddit_page, ":", type(reddit_page), ":"

# parse the json into python objects
parsed = json.loads(reddit_page.read())

print "parsed :", parsed, ":", type(parsed), ":"

num = 0
# iterate through every news item on the page
for item in parsed['data']['children']:
    # put it in mongo
    num += 1
    print num, ".) item :", item['data'], ":"
    stories.insert_one(item['data'])

