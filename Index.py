import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'gym_buddy'
app.config["MONGO_URI"] = 'mongodb+srv://murphya14:gymbuddy@gymbuddy-asswz.mongodb.net/gym_buddy?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/')

@app.route('/get_work_out')
def get_work_out():
    return render_template("work_out.html", 
    work_out=mongo.db.week1_day1.find())


@app.route('/add_excercise')
def add_excercise():
    return render_template("addexcercise.html",
    categories=mongo.db.category.find())


@app.route('/insert_excercise', methods=['POST'])
def insert_excercise():
    workout=mongo.db.week1_day1
    workout.insert_one(request.form.to_dict())
    return redirect(url_for('get_work_out'))

@app.route('/edit_weight/<week1_day1_id>' )
def insert_weight(week1_day1_id):
    the_weight =  mongo.db.week1_day1.find_one({"_id": ObjectId(week1_day1_id)})
    return render_template('edit_weight.html', weight=the_weight)


@app.route('/update_weight/<week1_day1_id>', methods=["POST"])
def update_weight(week1_day1_id):
    workout = mongo.db.week1_day1
    workout.update( {'_id': ObjectId(week1_day1_id)},
    {
         'main_weight':request.form.get('main_weight')
    })
    return redirect(url_for('work_out'))

print(os.environ.get('PORT'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 8000)),
            debug=True)