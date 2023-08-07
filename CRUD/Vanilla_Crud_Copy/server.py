from flask import Flask
app = Flask(__name__)
app.secret_key = ";poajsjhnfvoengoltnhodchboasih"
from flask import request, render_template, redirect
from models.user import User


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create/user", methods = ['POST'])
def create_new_user():
    User.create_user(request.form)
    return redirect("/show")

@app.route("/show")
def show_all_users():
    all_users = User.get_all_users()
    print(all_users)
    return render_template("show.html", all_users = all_users)

@app.route("/update/<int:id>")
def update_form(id):
    data = {"id": id}
    one_user = User.get_one_user_by_id(data)
    print(one_user)
    return render_template("update.html", user = one_user)

@app.route("/update/user", methods = ['POST'])
def update_user():
    data = {
        "id": request.form['id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "about": request.form['about']
    }
    if User.update_user_by_id(data) == None:
        return redirect("/show")
    else:
        return redirect(f"/update/{request.form['id']}")
    
@app.route("/delete/<int:id>")
def delete_user(id):
    data = {"id": id}
    User.delete_user_by_id(data)
    return redirect("/show")








if __name__ == "__main__":
    app.run(debug = True)