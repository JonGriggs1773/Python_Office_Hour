from flask import Flask
app = Flask(__name__)
app.secret_key = "'adpsofjgbw'p4rl6lnmt6bpirjbvp"
from flask import request, render_template, redirect
from models.user import User



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create/user", methods = ['POST'])
def create_new_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "about": request.form['about']
    }
    User.create_user(data)
    return redirect("/")


@app.route("/show/users")
def show_users():
    all_users = User.get_all_users()
    return render_template("read.html", users = all_users)











if __name__ == "__main__":
    app.run(debug=True)