import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'gym_buddy'
app.config["MONGO_URI"] = 'mongodb+srv://murphya14:gymbuddy@gymbuddy-asswz.mongodb.net/week1_day1?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/')

@app.route('/get_warm_up')
def get_tasks():
    return render_template("warm_up.html", 
    warm_up=mongo.db.week1_day1.find())


@app.route('/add_excercise')
def add_excercise():
    return render_template("addexcercise.html")

print(os.environ.get('PORT'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 8000)),
            debug=True)