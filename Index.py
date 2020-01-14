import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "super secret key" 
app.config["MONGO_DBNAME"] = 'gym_buddy'
app.config["MONGO_URI"] = 'mongodb+srv://murphya14:gymbuddy@gymbuddy-asswz.mongodb.net/gym_buddy?retryWrites=true&w=majority'
mongo = PyMongo(app)
comment=[] #for add comment (need to make function)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
            user_name = request.form.get("name")
            user_id = mongo.db.user.find_one({'name': user_name})["_id"] 
            user =  mongo.db.user.find_one({"_id": ObjectId(user_id)})
            session["user"] = user

    if "user" in session:
        return redirect(url_for('get_user'))

    return render_template("index.html",
    user=mongo.db.user.find())

@app.route('/get_user/<user_name>', methods=["GET", "POST"])
def get_user(user_name):
   
    ''' Function gets the user ID and name '''
    user_name = request.form.get("name")
    user = session["user"]     
    # find by form 'name', and get the ["_id"] from db
    # user = mongo.db.user.find_one({'_id': ObjectId(id)}) # this one doesn't print anything
    print(user) # print result in terminal to see which _id is returned
    work_out=mongo.db.week1_day1.find()
    return render_template("work_out.html", user_name=user_name, user=user, work_out=work_out)

@app.route('/add_excercise')
def add_excercise():
    return render_template("addexcercise.html",
    categories=mongo.db.category.find())

@app.route('/insert_excercise', methods=['POST'])
def insert_excercise():
    workout=mongo.db.week1_day1
    workout.insert_one(request.form.to_dict())
    return redirect(url_for('get_user'))

@app.route('/edit_excercise/<week1_day1_id>' )
def edit_excercise(week1_day1_id):
    the_weight =  mongo.db.week1_day1.find_one({"_id": ObjectId(week1_day1_id)})
    return render_template('edit_weight.html', weight=the_weight)

@app.route('/update_excercise/<week1_day1_id>', methods=["POST"])
def update_excercise(week1_day1_id):
    workout = mongo.db.week1_day1
    workout.update( {'_id': ObjectId(week1_day1_id)},
    {
         'main_weight':request.form.get('main_weight')
    })
    return redirect(url_for('get_user'))


#  This is the USER

# name, week1_day1, weight

# def addUser  - GET and POST


@app.route('/add_user')
def add_user():
    return render_template("signup.html",
    workout=mongo.db.week1_day1.find(),
    user=mongo.db.user.find())


@app.route('/insert_user', methods=['POST'])
def insert_user():
    user=mongo.db.user
    user.insert_one(request.form.to_dict())
    return redirect(url_for('get_user'))

# def editUser - GET and POST

@app.route('/edit_user/<user_name>' )
def edit_user(user_name):
    user_id = mongo.db.user.find_one({'name': user_name})["_id"]
    print(user_id)
    user =  mongo.db.user.find_one({"_id": ObjectId(user_id)})
    the_workout = mongo.db.week1_day1.find()
    return render_template('edit_user.html', user=user, workout=the_workout, user_id=user_id)

@app.route('/update_user/<user_id>', methods=["POST"])
def update_user(user_id):
    users = mongo.db.user
    users.update( {'_id': ObjectId(user_id)},
    {
    'name':request.form.get('name'),
    'week':request.form.get('week'),
    'weight':request.form.get('weight'),
    })
    return redirect(url_for('get_user'))

# Once complete is selected => bring to edit user page where you can select yourself (the user) - this will keep track of where everyone is in the program

print(os.environ.get('PORT'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 8000)),
            debug=True)