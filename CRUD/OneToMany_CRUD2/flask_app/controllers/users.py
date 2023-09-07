from flask_app import app
from flask import request, render_template, redirect, session
from flask_app.models.user import User


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create/user/submission", methods = ['POST'])
def create_new_user():
    if User.create_user(request.form):
        return redirect("/view/all_users")
    else:
        return redirect("/")
    
@app.route("/login/user", methods = ['POST'])
def login():
    if User.login_user(request.form):
        return redirect('/view/all_users')
    else:
        return redirect('/')

@app.route("/uglyform")
def uglyform():
    return render_template("index_terribad.html")


@app.route("/view/all_users")
def show_all_users_with_pets():
    if 'user_id' in session:
        logged_in_user = User.get_one_user_by_id(session['user_id'])
        all_users_with_pets = User.get_all_users_with_pets()
        print(all_users_with_pets)
        return render_template("all_users.html", all_users = all_users_with_pets, logged_in_user=logged_in_user)
    else:
        return redirect("/")

@app.route("/view/user/<int:user_id>")
def show_one_user_with_pets(user_id):
    data = {
        'id': user_id
    }
    one_user_with_pets = User.get_one_user_with_pets(data)
    if one_user_with_pets:
        return render_template("one_user.html", user = one_user_with_pets)
    else:
        return redirect("/view/all_users")

@app.route("/update/user/<int:id>")
def update_form(id):
    data = {"id": id}
    one_user = User.get_one_user_by_id(data)
    print(one_user)
    return render_template("update.html", user = one_user)

@app.route("/update/user/submission", methods = ['POST'])
def update_user():
    data = {
        "id": request.form['id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "about": request.form['about']
    }
    if User.update_user_by_id(data) == None:
        return redirect("/view/all_users")
    else:
        return redirect(f"/update/user/{request.form['id']}")
    
@app.route("/delete/user/<int:id>")
def delete_user(id):
    data = {"id": id}
    User.delete_user_by_id(data)
    return redirect("/view/all_users")

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')