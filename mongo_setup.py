from flask import Flask,request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.flask_db
users = db.users
posts = db.posts

def getCollections():
    return {
        'users': users,
        'posts': posts
    }
