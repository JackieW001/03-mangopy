'''
Name: Catalan Historical Events Dataset
Our dataset contains the date and the event that occured on that date in the Catalan language. For example, the second entry of this dataset states that in the year -300, the first documented meteorological forecast was written by Teofrasto. 

Hyperlink: 
http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=ca

Import mechanism:
We made each event a separate collection in the Cieres database.

'''

import pymongo
import json
from pprint import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

teamname = 'wooJ-tabassumM'

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection[teamname]
collection = db['catalan']

filename = "catalan.json"
f = open(filename,'r').read()

def join_duplicate_keys(ordered_pairs):
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           if type(d[k]) == list:
               d[k].append(v)
           else:
               newlist = []
               newlist.append(d[k])
               newlist.append(v)
               d[k] = newlist
        else:
           d[k] = v
    return d

newdict = json.loads(f, object_pairs_hook=join_duplicate_keys)

el = newdict['result']

def updateDB(event_list):
    for x in el['event']:
        #print x
        date = x['date']
        #print date
        description = x['description']
        #print description
        lang = x['lang']
        #print lang
        granularity = x['granularity']
        #print granularity
        db.collection.insert({'date': date, "description": description, 'lang': lang, 'granularity': granularity})
        print "added successfully"

#print el
#updateDB(el)




#Adding to Database
#collection.insert_many(el)


#Searching by date
def date(d):
    c = db.collection.find({'date': d})
    for i in c:
        print i

print "----- Seaching by Date ----"
date('-300')


def desc(d):
    c = db.collection.find({'description':d})
    for i in c:
        print i

print "---- Searching by Description ---"
desc('Auge de Meroe')

'''
# Not that useful

def gran(g):
    c = db.collection.find({'granularity':g})
    for i in c:
        print i
gran('year')


def lang(l):
    c = db.collection.find({'lang':l})
    for i in c:
        print i
lang('ca')
'''
