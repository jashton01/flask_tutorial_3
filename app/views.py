from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/client_create")
def client_create():
    return render_template("public/client_create.html")


#adding something

@app.route("/about")
def about():
    return render_template("admin/dashboard.html")
