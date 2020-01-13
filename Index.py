import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "super secret key" #change this
app.config["MONGO_DBNAME"] = 'gym_buddy'
app.config["MONGO_URI"] = 'mongodb+srv://murphya14:gymbuddy@gymbuddy-asswz.mongodb.net/gym_buddy?retryWrites=true&w=majority'
mongo = PyMongo(app)
comment=[] #for add comment (need to make function)

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html",
    user=mongo.db.user.find())

@app.route('/get_user', methods=["GET", "POST"])
def get_user():
    ''' Function gets the user ID and name '''
    user_name = request.form.get("name")
    user = mongo.db.user.find_one({'name': user_name})["_id"] # find by form 'name', and get the ["_id"] from db
    # user = mongo.db.user.find_one({'_id': ObjectId(id)}) # this one doesn't print anything
    print(user) # print result in terminal to see which _id is returned
    work_out=mongo.db.week1_day1.find()
    return render_template("work_out.html", user_name=user_name, user=user, work_out=work_out)
    


@app.route('/get_work_out')
def get_work_out():
    if 'logged' in session:
        current_user = session['name']
        flash('Hi "' + current_user + '". Welcome back! ' +
                'Here is your current workout' , 'success')

        #find the user
        user_name = request.form.get("name") 
        user = mongo.db.user.find_one({'name': user_name})["_id"]
        
        
        workout = mongo.db.workout.find({'name': current_user})
        count = mongo.db.workout.count_documents({'name': current_user})


        return render_template("work_out.html", 
        work_out=workout,
        user = user,
        count=count)

    else:
            # if user is not created
            flash('You need to be logged in to see your workout', 'warning')
            return redirect(url_for('signup'))


@app.route('/add_excercise')
def add_excercise():
    return render_template("addexcercise.html",
    categories=mongo.db.category.find())

@app.route('/insert_excercise', methods=['POST'])
def insert_excercise():
    workout=mongo.db.week1_day1
    workout.insert_one(request.form.to_dict())
    return redirect(url_for('get_work_out'))

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
    return redirect(url_for('work_out'))


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
    return redirect(url_for('get_work_out'))

# def editUser - GET and POST

@app.route('/edit_user/<user_name>' )
def edit_user(user_name):
    user_id= mongo.db.user.find_one({'name': user_name})["_id"]
    print(user_name)
    the_workout = mongo.db.week1_day1.find()
    return render_template('edit_user.html', user=user_id, workout=the_workout)

@app.route('/update_user/<user>', methods=["POST"])
def update_user(user):
    user_name = request.form.get("name") 
    user = mongo.db.user.find_one({'name': user_name})["_id"]
    user.update( {'_id': ObjectId(user)},
    {
    'name':request.form.get('name'),
    'week':request.form.get('week'),
    'weight':request.form.get('weight'),
    })
    return redirect(url_for('work_out'))

# Once complete is selected => bring to edit user page where you can select yourself (the user) - this will keep track of where everyone is in the program

print(os.environ.get('PORT'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 8000)),
            debug=True)