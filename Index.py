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
        session["name"] = request.form["name"]
        name=session["name"] 
        user = mongo.db.user.find_one({'name': name})
        
        user_id=user['_id']
        print(user_id)
        return redirect(url_for('get_user', user_id=user_id))

    if "name" in session:
        name=session["name"] 
        user = mongo.db.user.find_one({'name': name})
        user_id=user['_id']
       
        return redirect(url_for('get_user', user_id=user_id))
   

    return render_template("index.html",
    user=mongo.db.user.find(), users=mongo.db.user.find())

@app.route('/get_user/<user_id>', methods=["GET", "POST"])
def get_user(user_id):
    user= mongo.db.user.find_one({"_id": ObjectId(user_id)})
    user_week=user['week']
    workout=  mongo.db.week1_day1.find_one({"week": user_week})
    
    
    if "name" not in session:
        return redirect(url_for('home'))

    return render_template("work_out.html", user=user, workout=workout, user_id=user_id, user__id=user_id)


@app.route('/edit_weight/<user_id>' )
def edit_weight(user_id):
    user= mongo.db.user.find_one({"_id": ObjectId(user_id)})
    user_week=user['week']
    workout=  mongo.db.week1_day1.find_one({"week": user_week})
    return render_template('edit_weight.html', workout=workout, user_id=user_id, user=user, user_week=user_week)

@app.route('/update_weight/<user_id>', methods=["POST"])
def update_weight(user_id):
    users = mongo.db.user
    
    users.update(
                {'_id': ObjectId(user_id)},
                    {"$set":
                        {
                        'benchpress':request.form.get('benchpress'),
                        'squat':request.form.get('squat')
                        }
                    }
                )
                   #check and do it for all the main weights 
    return redirect(url_for('get_user', user_id=user_id))

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

@app.route('/edit_user/<user_id>' )
def edit_user(user_id):
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

    return redirect(url_for('get_user', user_id=user_id))


@app.route('/delete_user/<user_id>', methods=["POST"])
def delete_user(user_id):
    mongo.db.user.remove({'_id': ObjectId(user_id)})
    return redirect(url_for('home'))


print(os.environ.get('PORT'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 8000)),
            debug=True)