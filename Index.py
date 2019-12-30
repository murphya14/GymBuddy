import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'gym_buddy'
app.config["MONGO_URI"] = 'mongodb+srv://murphya14:Quality@2@gymbuddy-asswz.mongodb.net/gym_buddy?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_warm_up')
def get_tasks():
    return render_template("warm_up.html", warm_up=mongo.db.week1_day1.warm_up.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)