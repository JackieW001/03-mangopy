import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")

db = connection['test']
collection = db['restaurants']

def print_collection():
    c = collection.find()
    for i in c:
        print i
        print ""
        
def borough_search( b ):
    
    c = collection.find({'borough': b})
    
    for i in c:
        print i
        print " "
        
print " ----------------- BOROUGH SEARCH --------------------------"
borough_search('Manhattan')

def zip_search( z ):
    
    c = collection.find({'address.zipcode': z})
    
    for i in c:
        print i
        print " "

print " ----------------ZIPCODE SEARCH ----------------------------"
zip_search('10282')


def zip_grade_search( z,g ):
    
    c = collection.find({'address.zipcode': z, 'grades.grade': g})
    
    for i in c:
        print i
        print " "

print " ------------ZIPCODE AND GRADE SEARCH ----------------------"
zip_grade_search('10282', 'A')


def zip_score_search( z,s ):

    c = collection.find({
        'address.zipcode': z,
        'grades.score': {'$lt':s}
    })
    
    for i in c:
        print i
        print " "

print " ------------ZIPCODE AND SCORE SEARCH ----------------------"
zip_score_search('10282', 10)

def cuisine_borough_score_search( cus,b,s):
    c = collection.find({
        'cuisine': cus,
        'borough': b,
        'grades.score': {'$gt':s}
    })
    
    for i in c:
        print i
        print " "

print "------------ SPECIALTY ----------------------"
cuisine_borough_score_search('Italian', 'Manhattan', 10)
