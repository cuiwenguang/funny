import pymongo
import motor
from conf.settings import mongo


mongo = pymongo.MongoClient("10.20.22.131")["fun_db"]


users = mongo["users"]

articles =  mongo["articles"]

comments = mongo["comments"]

favorites = mongo["favorites"]