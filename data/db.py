import pymongo
import motor
from conf.settings import mongo


mongo = pymongo.MongoClient("localhost")["fun_db"]


users = mongo["users"]

articles =  mongo["articles"]

comments = mongo["comments"]