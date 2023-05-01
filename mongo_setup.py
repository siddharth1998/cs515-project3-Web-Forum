from flask import Flask,request
from pymongo import MongoClient,TEXT

client = MongoClient('localhost', 27017)
db = client['project-3-database']

users = db.users
posts = db.posts
db.posts.create_index([('msg', TEXT)])
def getCollections():
    return {
        'users': users,
        'posts': posts
    }
