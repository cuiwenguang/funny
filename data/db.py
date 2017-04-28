import pymongo
import motor
from conf.settings import mongo


mongo = pymongo.MongoClient("10.20.22.131")["fun_db"]

users = mongo["users"]

