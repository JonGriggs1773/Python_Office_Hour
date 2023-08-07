from flask import Flask
app = Flask(__name__)
app.secret_key = "This key is a secret."