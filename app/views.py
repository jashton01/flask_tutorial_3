from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("public/index2.html")

@app.route("/client_create")
def client_create():
    return render_template("public/client_create.html")


#adding something

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """
