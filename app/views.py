from app import app
from flask import render_template
from flask import request, redirect
from createsend import Subscriber

account_auth = {'api_key':'/7k+rgSybkxGMa64aUb+DPuAGpM5NxC3EjanNlSDjrRom3gKTHe6Z/t5GOJA9IlditAvifnjymZGVH6ZW1xqYE5EnuoJBr9hWXn7yscIZOyoeoJjugUcGix/fb8V2lzJIG+ab56sLijjsgL49KGvWw=='}
client_auth = {'api_key':'otYR1hX2Rwul5NfryE/34LF2dpnEq54yCYn3ezdGVsEx5m6Ii3JJ0xp1+RpBPsnD2M3Nw7O2fkWTfZTFhGsK6YfZ2bFe2q/f0BVMLC1M08x45xlTEi3KSzjzASFxtxp0Wlepoi9SVYr6ga/vF7bd4A=='}

def add_subscriber(username):
    my_subscriber = Subscriber(client_auth)
    custom_fields = [{"Key": 'username', "Value": username}]
    my_subscriber.add("7c480b336839fbba731ca50c5d269666", "jashton+api8@sailthru.com", username, custom_fields, True, "yes")
    print("success")

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/client_create")
def client_create():
    return render_template("public/client_create.html")


#adding something

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form
        missing = list()
        for k, v in req.items():
            if v == "":
                missing.append(k)
        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("public/sign_up.html", feedback=feedback)

        req = request.form
        print("Your response is:", req)
        user_name = req['username']
        add_subscriber(username=user_name)
        return redirect(request.url)


    return render_template("public/sign_up.html")

@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/jinja")
def jinja():
    my_name = "Julian"

    # Integers
    my_age = 23

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    # Dictionaries
    friends = {
        "Tony": 43,
        "Cody": 28,
        "Amy": 26,
        "Clarissa": 23,
        "Wendell": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    return render_template(
    "public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
    friends=friends, colors=colors, cool=cool, GitRemote=GitRemote,
    my_remote=my_remote, repeat=repeat
)
