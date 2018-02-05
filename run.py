import pymongo
from pymongo import MongoClient
from bson import ObjectId
from pprint import pprint

client = MongoClient('localhost',8201)
db = client.indeedspotmentor
db_data = db.data.find({'$or' : [{'_id'  : ObjectId('58eb9973f7c05500123a870d')}, {'skills' : {'$in' : ['python' , 'R']}}]})


indeed_data = []
for data in db_data:
	indeed_data.append(data.get('work_experience'))

print 'No of resumes: ', db_data.count()

i=0
for item in indeed_data:
	for value in item:
		print 'work title: ', value.get('work_title')
		print 'work company: ', value.get('work_company')
		i += 1

print 'No of work titles: ', i
import ipdb;ipdb.set_trace()