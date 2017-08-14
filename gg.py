# python -m pip install pymongo
# python -m pip install pymongo[gssapi,tls]

# Making a Connection with MongoClient
from pymongo import MongoClient
client = MongoClient("mongodb://pega:pega@122.116.71.79/pega")

db = client.pega
posts = db.posts

import datetime
##post = {"author": "GG",
##"text": "haha",
##"tags": ["mongodb", "python", "pymongo"],
##"date": datetime.datetime.utcnow()}
##post_id = posts.insert_one(post).inserted_id
##post_id




import pprint
#pprint.pprint(posts.find_one())
for post in posts.find({}):
	pprint.pprint(post)




#new_posts = [{"author": "Mike",
# "text": "Another post!",
# "tags": ["bulk", "insert"],
# "date": datetime.datetime(2009, 11, 12, 11, 14)},
#{"author": "Eliot",
# "title": "MongoDB is fun",
# "text": "and pretty easy too!",
# "date": datetime.datetime(2009, 11, 10, 10, 45)}]
#result = posts.insert_many(new_posts)
#result.inserted_ids


print posts.count({"author": "Mike"})

db.posts.find_one({'author': 'GG'})
# db.posts.find_one({'author': 'Mike'},projection={'author': True, '_id': False})
aa = db.posts.find_one({'author': 'Mike'},projection={'author': True})

# db.posts.find_one_and_update(
# {'author': 'GG'},
# {'$inc': {'seq': 1}},
# projection={'seq': True, '_id': False},
# upsert=True,
# return_document=ReturnDocument.AFTER)

# modified
posts.update(
	{'author': 'Mike'},
	{'$unset': {'flag':'done'}}
)
