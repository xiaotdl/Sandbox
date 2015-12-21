# ref: http://api.mongodb.org/python/current/tutorial.html
#      http://api.mongodb.org/python/current/examples/index.html
# PyMongo 3.2
import datetime
import pymongo


# This tutorial assumes that a MongoDB instance is running on the default host and port.
# Assuming you have downloaded and installed MongoDB, you can start it like so:
#     $ mongod


# Making a Connection with MongoClient
client = pymongo.MongoClient('localhost', 27017)

# Getting a Database
db = client.test_database

# Getting a Collection
collection = db.test_collection

# Documents
# Note that documents can contain native Python types (like datetime.datetime instances)
# which will be automatically converted to and from the appropriate BSON types.
post = {'author': 'Mike',
        'text': 'My first blog post!',
        'tags': ['mongodb', 'python', 'pymongo'],
        'date': datetime.datetime.utcnow()}

# Inserting a Document
db.posts.drop()  # clean db collection "posts"
posts = db.posts # create db collection "posts"
post_id = posts.insert_one(post).inserted_id
# verify this by listing all of the collections in our database
print db.collection_names(include_system_collections=False)
# >>>
# [u'posts']

# Getting a Single Document With find_one()
print posts.find_one()
print posts.find_one({'author': 'Mike'})
print posts.find_one({'author': 'Eliot'})
# {u'date': datetime.datetime(2015, 12, 21, 7, 39, 42, 738000), u'text': u'My first blog post!', u'_id': ObjectId('5677acbe1748c0f054c4cc30'), u'author': u'Mike', u'tags': [u'mongodb', u'python', u'pymongo']}
# {u'date': datetime.datetime(2015, 12, 21, 7, 39, 42, 738000), u'text': u'My first blog post!', u'_id': ObjectId('5677acbe1748c0f054c4cc30'), u'author': u'Mike', u'tags': [u'mongodb', u'python', u'pymongo']}
# None

# Querying By ObjectId
# Note that an ObjectId is not the same as its string representation
print posts.find_one({'_id': post_id})
# A common task in web applications is to get an ObjectId from the request URL
# and find the matching document. It's necessary in this case to convert the ObjectId
# from a string before passing it to find_one:
# The web framework gets post_id from the URL and passes it as a string
from bson.objectid import ObjectId
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})

# A Note On Unicode Strings
# You probably noticed that the regular Python strings we stored earlier look different
# when retrieved from the server (e.g. u'Mike' instead of 'Mike'). A short explanation is in order.

# Bulk Inserts
# Note that new_posts[1] has a different "shape" than the other posts -
# there is no "tags" field and we've added a new field, "title".
# This is what we mean when we say that MongoDB is schema-free.
new_posts = [{'author': 'Mike',
              'text': 'Another post!',
              'tags': ['bulk', 'insert'],
              'date': datetime.datetime(2009, 11, 12, 11, 14)},
             {'author': 'Eliot',
              'title': 'MongoDB is fun',
              'text': 'and pretty easy too!',
              'date': datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
print result.inserted_ids
# >>>
# [ObjectId('...'), ObjectId('...')]

# Querying for More Than One Document
for post in posts.find():
    print post
for post in posts.find({"author": "Mike"}):
    print post

# Counting
print posts.count()
print posts.find({"author": "Mike"}).count()
# >>>
# 3
# 2

# Range Queries
# Here we use the special "$lt" operator to do a range query,
# and also call sort() to sort the results by author.
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    print post

# Indexing
# Adding indexes can help accelerate certain queries,
# and can also add additional functionality to querying and storing documents.
db.profiles.drop()  # clean db collection "posts"
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
                                  unique=True)
print list(db.profiles.index_information())
# >>>
# [u'user_id_1', u'_id_']
user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}
]
result = db.profiles.insert_many(user_profiles)
new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)       # This is fine.
result = db.profiles.insert_one(duplicate_profile) # This is not fine.
# >>>
# Traceback (most recent call last):
# pymongo.errors.DuplicateKeyError: E11000 duplicate key error index: test_database.profiles.$user_id_1 dup key: { : 212 }


