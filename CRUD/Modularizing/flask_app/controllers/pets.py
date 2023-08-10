from flask_app import app
from flask import request, render_template, redirect
from flask_app.models.pet import Pet
from flask_app.models.user import User

@app.route("/create/pet")
def create_pet_form():
    users = User.get_all_users()
    return render_template("create_pet.html", users = users)

@app.route("/create/pet/submission", methods = ['POST'])
def create_new_pet():
    Pet.create_pet(request.form)
    return redirect("/view/all_users")