# -*- coding:utf-8 -*-
import pymongo
import sys
#连接mongo
if(len(sys.argv) != 3):
    print("usage: python3 mongo-del-emptyColl.py 127.0.0.1:27017 db_name")
    sys.exit()
addr = sys.argv[1]
db_name = sys.argv[2]
myclient = pymongo.MongoClient("mongodb://"+ addr + "/")
mydb = myclient[db_name]

#列出所有表,并删除所有空coll
collist = mydb.list_collection_names()
for coll in collist:
    if  mydb[coll].find_one({}) == None:
        print(coll)
        mydb[coll].drop()
print("All Empty Collections are deleted.")

