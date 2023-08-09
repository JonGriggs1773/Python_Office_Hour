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
    return redirect("/view/all")

# @app.route("/view/all")
# def show_all_users():
#     all_users = User.get_all_users()
#     print(all_users)
#     return render_template("all_users.html", all_users = all_users)

# @app.route("/view/<int:user_id>")
# def show_one_user(user_id):
#     data = {
#         'id': user_id
#     }
#     user = User.get_one_user_by_id(data)
#     print(user)
#     if user:
#         return render_template("one_user.html", user = user)
#     else:
#         return redirect("/view/all")

# @app.route("/update/<int:id>")
# def update_form(id):
#     data = {"id": id}
#     one_user = User.get_one_user_by_id(data)
#     print(one_user)
#     return render_template("update.html", user = one_user)

# @app.route("/update/user", methods = ['POST'])
# def update_user():
#     data = {
#         "id": request.form['id'],
#         "first_name": request.form['first_name'],
#         "last_name": request.form['last_name'],
#         "email": request.form['email'],
#         "about": request.form['about']
#     }
#     if User.update_user_by_id(data) == None:
#         return redirect("/view/all")
#     else:
#         return redirect(f"/update/{request.form['id']}")
    
# @app.route("/delete/<int:id>")
# def delete_user(id):
#     data = {"id": id}
#     User.delete_user_by_id(data)
#     return redirect("/view/all")

# @app.route('/show_one_user_with_pets/<int:id>')
# def show_one_user_with_pets(id):
#     data = {"id": id}
#     one_user_with_pets = User.get_one_user_by_id(data)
#     print(one_user_with_pets)
#     return render_template("one_user.html", user = one_user_with_pets)