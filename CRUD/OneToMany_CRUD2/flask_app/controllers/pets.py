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

# @app.route("/view/all")
# def show_all_users():
#     all_users = User.get_all_users()
#     print(all_users)
#     return render_template("all_users.html", all_users = all_users)

@app.route("/view/pet/<int:pet_id>")
def show_one_pet_with_owner(pet_id):
    data = {
        'id': pet_id
    }
    pet = Pet.get_one_pet_with_user(data)
    print(pet)
    if pet:
        return render_template("one_pet.html", pet = pet)
    else:
        return redirect("/view/all_users")

@app.route("/update/pet/<int:id>")
def update_pet_form(id):
    data = {"id": id}
    one_pet = Pet.get_one_pet_by_id(data)
    users = User.get_all_users()
    print(one_pet.__dict__)
    return render_template("update_pet.html", users = users, pet = one_pet)

@app.route("/update/pet/submission", methods = ['POST'])
def update_pet():
    data = {
        "id": request.form['id'],
        "name": request.form['name'],
        "species": request.form['species'],
        "how_many_legs": request.form['how_many_legs'],
        "friendly": request.form['friendly'],
        "user_id": request.form['user_id']
    }
    if Pet.update_pet_by_id(data) == None:
        return redirect("/view/all_users")
    else:
        return redirect(f"/update/pet/{request.form['id']}")
    
@app.route("/delete/pet/<int:id>")
def delete_pet(id):
    data = {"id": id}
    Pet.delete_pet_by_id(data)
    return redirect("/view/all_users")